# Secret Santa QR

Simple python script for drawing secret Santas.
The script creates a QR code for every name given.
In the QR code is the assignment. (See [example](#example))

The main idea is to do the drawing for secret Santa without needing everyone
to be at the same place, and without everyone to give out their email or phone number.
Just run the script, and send everyone the file with their name.
The recipients then just need to read the QR code to see who they have got assigned.

## Installation
```
pip install -r requirements.txt
```

## Usage
```
python secret_santa.py Alice Bob Charlie Dora <other names>
```

## Example
Running
```
python secret_santa.py Alice Bob Charlie Dora
```
Will create 4 files: 
- [Alice.png](./example/Alice.png) -> Got Charlie 
- [Bob.png](./example/Bob.png) -> Got Alice
- [Charlie.png](./example/Charlie.png) -> Got Dora
- [Dora.png](./example/Dora.png) -> Got Bob