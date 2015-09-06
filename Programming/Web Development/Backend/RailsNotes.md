These are [David Coven's](github.com/mrcoven94) person notes as derived from Michael Hartl's awesome tutorial. The context is developing Ruby on Rails web applications using the [c9.io](c9.io) cloud based editor.

#### Running c9.io server
```ruby
rails s -p $PORT -b $IP
```
#### Running Jekyll on c9.io server
```ruby
jekyll serve --host $IP --port $PORT --baseurl ''
```
#### Adding admin permission via rails console
```ruby
U = User.find(1)
U.update_attribute :status, "admin"
```

#### Adding Image with Paperclip 
After you fill in the paperclip gem, and run bundle install, make sure ImageMagick is installed via

```git
sudo apt-get install imagemagick  
```

#### Configure Git
```git
$ git config --global user.name "Your Name"
$ git config --global user.email your.email@example.com
$ git config --global push.default matching
$ git config --global alias.co checkout
```
#### Configure BitBucket
1. Sign up for a Bitbucket account if you don’t already have one.
2. Copy your public key to your clipboard. As indicated in Listing 1.11, users of the cloud IDE can view their public key using the cat command, which can then be selected and copied. If you’re using your own system and see no output when running the command in Listing 1.11, follow the instructions on how to install a public key on your Bitbucket account.
3. Add your public key to Bitbucket by clicking on the avatar image in the upper right and selecting “Manage account” and then “SSH keys” 
4. Create” to create a new repository 
5. Leave the box next to “This is a private repository.” checked. 
6. After clicking “Create repository”, follow the instructions under “Command line > I have an existing project”
7. When pushing up the repository, answer yes if you see the question “Are you sure you want to continue connecting (yes/no)?”

Listing 1.11 
```git 
$ cat ~/.ssh/id_rsa.pub
```
Adding Bitbucket and pushing up the repository.
```git 
$ git remote add origin git@bitbucket.org:<username>/hello_app.git
$ git push -u origin --all # pushes up the repo and its refs for the first time
```

#### Configure Heroku
```git
$ heroku version
$ heroku login
$ heroku keys:add
```
Creating a new application at Heroku.
```
$ heroku create
$ git push heroku master
```

Rename Heroku App

```
$ heroku apps:rename newname
```
And then you should see the following in your command line

```
Renaming oldname to newname... done
http://newname.herokuapp.com/ | git@herokuapp.com:newname.git
Git remote heroku updated
```

Sometimes you may get an error saying that it cannot find the app, and that you have to specify. In this case run ```--app APP```. For example I want to rename my app from **whispering-peak-4146** to **recommend-coven**. To do this I run the following.
```
$ heroku apps:rename recommend-coven --app whispering-peak-4146
```

#### initialize  & Push to Git repo
```git
$ git init
$ git add -A
$ git commit -m "Initialize repository"
$ git remote add origin git@bitbucket.org:<username>/sample_app.git
$ git push -u origin --all # pushes up the repo and its refs for the first time
```
#### Push to Heroku repo
```git
$ git commit -am "Add hello"
$ heroku create
$ git push heroku master
```

<hr>
#### Undoing things
Even when you’re very careful, things can sometimes go wrong when developing Rails applications. One common scenario is wanting to undo code generation—for example, when you change your mind on the name of a controller and want to eliminate the generated files. Because Rails creates a substantial number of auxiliary files along with the controller, this isn’t as easy as removing the controller file itself; undoing the generation means removing not only the principal generated file, but all the ancillary files as well.  In particular, these two commands cancel each other out:
```ruby
  $ rails generate controller StaticPages home help
  $ rails destroy  controller StaticPages home help
```

Generating a model can be undone by:
```ruby
  $ rails generate model User name:string email:string
  $ rails destroy model User

```

Undoing migrations. Migrations change the state of the database using the command
```ruby
  $ bundle exec rake db:migrate
  $ bundle exec rake db:rollback
```
To go all the way back to the beginning, we can use
```ruby
  $ bundle exec rake db:migrate VERSION=0
```
Substituting any other number for 0 migrates to that version number, where the version numbers come from listing the migrations sequentially.

#### Error Handling
##### MiniTest reporters
Makes default Rails tests show red and green at the appropriate times. You can find the file in ```test/test_helper.rb```
```ruby
ENV['RAILS_ENV'] ||= 'test'
require File.expand_path('../../config/environment', __FILE__)
require 'rails/test_help'
require "minitest/reporters"
Minitest::Reporters.use!

class ActiveSupport::TestCase
  # Setup all fixtures in test/fixtures/*.yml for all tests in alphabetical
  # order.
  fixtures :all

  # Add more helper methods to be used by all tests here...
end
```
##### Backtrace silencer
Add this to the file ```config/initializers/backtrace_silencers.rb```
```ruby
# Be sure to restart your server when you modify this file.

# You can add backtrace silencers for libraries that you're using but don't
# wish to see in your backtraces.
Rails.backtrace_cleaner.add_silencer { |line| line =~ /rvm/ }

# You can also remove all the silencers if you're trying to debug a problem
# that might stem from framework code.
# Rails.backtrace_cleaner.remove_silencers!
```

##### Automated tests with Guard
For this we need to build the actual Guard file. We can do that by running the following code. 
```git
$ bundle exec guard init
```
We then edit the resulting Guardfile so that Guard will run the right tests when the integration tests and views are updated 

```ruby
# Defines the matching rules for Guard.
guard :minitest, spring: true, all_on_start: false do
  watch(%r{^test/(.*)/?(.*)_test\.rb$})
  watch('test/test_helper.rb') { 'test' }
  watch('config/routes.rb')    { integration_tests }
  watch(%r{^app/models/(.*?)\.rb$}) do |matches|
    "test/models/#{matches[1]}_test.rb"
  end
  watch(%r{^app/controllers/(.*?)_controller\.rb$}) do |matches|
    resource_tests(matches[1])
  end
  watch(%r{^app/views/([^/]*?)/.*\.html\.erb$}) do |matches|
    ["test/controllers/#{matches[1]}_controller_test.rb"] +
    integration_tests(matches[1])
  end
  watch(%r{^app/helpers/(.*?)_helper\.rb$}) do |matches|
    integration_tests(matches[1])
  end
  watch('app/views/layouts/application.html.erb') do
    'test/integration/site_layout_test.rb'
  end
  watch('app/helpers/sessions_helper.rb') do
    integration_tests << 'test/helpers/sessions_helper_test.rb'
  end
  watch('app/controllers/sessions_controller.rb') do
    ['test/controllers/sessions_controller_test.rb',
     'test/integration/users_login_test.rb']
  end
  watch('app/controllers/account_activations_controller.rb') do
    'test/integration/users_signup_test.rb'
  end
  watch(%r{app/views/users/*}) do
    resource_tests('users') +
    ['test/integration/microposts_interface_test.rb']
  end
end

# Returns the integration tests corresponding to the given resource.
def integration_tests(resource = :all)
  if resource == :all
    Dir["test/integration/*"]
  else
    Dir["test/integration/#{resource}_*.rb"]
  end
end

# Returns the controller tests corresponding to the given resource.
def controller_test(resource)
  "test/controllers/#{resource}_controller_test.rb"
end

# Returns all tests for the given resource.
def resource_tests(resource)
  integration_tests(resource) << controller_test(resource)
end
```

Guard can get buggy and still  slow down processes. So we may have to manually clear them. 

##### Unix processes
On Unix-like systems such as Linux and OS X, user and system tasks each take place within a well-defined container called a process. To see all the processes on your system, you can use the ps command with the aux options:

```  
$ ps aux
```
To filter the processes by type, you can run the results of ps through the grep pattern-matcher using a Unix pipe |:

 ``` 
 $ ps aux | grep spring
 ```
  ubuntu 12241 0.3 0.5 589960 178416 ? Ssl Sep20 1:46
  spring app | sample_app | started 7 hours ago
The result shown gives some details about the process, but the most important thing is the first number, which is the process id, or pid. To eliminate an unwanted process, use the kill command to issue the Unix kill code (which happens to be 9) to the pid:

```  
$ kill -9 12241
```
This is the technique I recommend for killing individual processes, such as a rogue Rails server (with the pid found via ps aux | grep server), but sometimes it’s convenient to kill all the processes matching a particular process name, such as when you want to kill all the spring processes gunking up your system. In this particular case, you should first try stopping the processes with the spring command itself:

```  
$ spring stop
```
Sometimes this doesn’t work, though, and you can kill all the processes with name spring using the pkill command as follows:

```  
$ pkill -9 -f spring 
```
Any time something isn’t behaving as expected or a process appears to be frozen, it’s a good idea to run ps aux to see what’s going on, and then run kill -9 <pid> or pkill -9 -f <name> to clear things up.

