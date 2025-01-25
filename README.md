![BaseWoof](BaseWoof.png)

[![img](https://camo.githubusercontent.com/4b67cffa2993c78de4b80bccceb0183b2bbcea25425a1af7c531f11fe7cec460/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f6d616465253230776974682d507974686f6e332d626c756576696f6c6574)](https://www.python.org/) [![img](https://camo.githubusercontent.com/a4a7d4ba83399c8b2d941534f4db4a18155f3cf53cb28a576417b5b39451ab63/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f706c6174666f726d2d6f73782532466c696e757825324677696e646f77732d626c756576696f6c6574)](https://github.com/Protosec-Research/AutoGDB?tab=readme-ov-file#)

## overview

For every CTFer, we may come across strings that go through many layers of Base-encoding. And if we decode it manually, it will be very troublesome!!!!Look at here! This is a tool to recognizes the base encoding type automatically and decodes it.

## Installing:

If you are new to BaseWoof, clone our project first!

Then use this command to install the "Base 91" library.

```
pip install base91
```

## Start your Cracking!

Run <u>b4se_w00f.py</u> then input the strings to decode.

This is an example.

```
python .\b4se_w00f.py
Please enter the strings to decode: ZmxhZ3tUaDFzXzFzXzRuX2V4NG1wMWV9
Suspected encoding type：Base64
The1th layer：
flag{Th1s_1s_4n_ex4mp1e}
Suspected encoding type：Base85
The2th layer：
M#[(RAJJNR
Fail to detect to type of code!
The encoding type can not been recognized or the last layer has been reached!
```

## How to develop?

Feel free to modify its code after you clone it locally!

I also sincerely appreciate your effort in reporting the bugs and enhancing the completeness of the program.

## Additional

#### If this tool has helped you, welcome to star me~

