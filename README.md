# fort
v0.0.2

## About
Command line application created in python with json and sqlite to easy store password. The stored data will be encrypted so only the person with master key will be able to access it.<br>
The data will be stored at the execution location. So if you execute the program within USB drive path, the data will be stored in the drive. You can take your data anywhere with this.
- Note : The data will be stored at the execution path, so keep in mind where you execute/call program from.

## Installation
From PyPI
```
pip install pyfort
```

From github
```
# Clone project
git clone https://github.com/a-tharva/fort && cd fort

# Installation
python3 setup.py install

# Run setup
fort
```

## Usage
![fort](https://user-images.githubusercontent.com/70326109/147367275-7ca73375-a66b-48f1-ae13-8eee1638e7eb.gif)
```
fort
> Login  # Already created account

  > insert        # insert into database
  > display       # display whole database
  > get           # get selected password and decrypt it
  > logout        # logout of current acount
  
> Signup # Create new account
> Erase  # Delete account!!!
> Ctrl+C # Exit
```

## Development
Still working on this project.<br>
- The Erase functionality is currently not provided as it creates some issues, will add that in future.<br>
- Next version will store everything in sqlite database instead of storing user details in json file.<br>
- Copy Key option will be added to store key seperate as user want. 
<!-- - More functions like displaying * while typing password will be added after I finish some other projects.<br> -->

## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request.
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request


## License
Distributed under the MIT License. [License](https://github.com/a-tharva/Password-Manager/blob/master/LICENSE)
