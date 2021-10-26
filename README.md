# Password-Manager
Password Manager v1.0

![Capture password](https://user-images.githubusercontent.com/70326109/136650754-0cbf7a0d-d35c-4fac-87e3-cfe2d53b2ed8.PNG)


## About
Command line application Password Manager created in python with json and sqlite to store user data and encrypted passwords.

## Modules
cryptography - to encrypt data before saving in database
```
pip install cryptography
```
hashlib - to hash user password before storing in json file
```
pip install hashlib
```
colorama, termcolor - for color
```
pip install colorama
pip install termcolor
```

## Usage
```
--Login  #Already created account

  --insert        #insert into database
  --display       #display whole database
  --show          #show selected password and decrypt it
  --logout        #logout of current acount
  
--Signup #Create new account
--Erase  #Delete account!!!
```

## Development
Still working on this project.<br>
- The Erase functionality is currently not provided as it creates some issues, will add that in future.<br>
- More functions like displaying * while typing password will be added after I finish some other projects.<br>
- Next version will store everything in sqlite database instead of storing user details in json file.<br>
- Copy Key option will be added to store seperate as user want. 

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
