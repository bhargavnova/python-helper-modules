# Universal files converter

Developing a versatile Python script that serves as a universal file converter, capable of converting various file formats to different formats. This tool will provide users a seamless way to convert files such as documents, images, audio, and more, enabling compatibility across different applications and platforms.

## Features

1. srt-lrc #added by (@bhargavnova |github)
2. pdf-docx #added by (@harshjais369 |github)
3. txt-csv #added by (@kom-senapati |github)
4. md-html #added by (@kom-senapati |github)

## Usage

```python
python convert_me.py -f srt-lrc -i zen_of_python.srt -o zen_of_python.lrc
```

## Installation

pip install -r requirements.txt

## Contributing Guidelines

# Important Note:
- It's not a single person's job to write this script, I am adding this as an issue so that you can comment first, on what you can add, and work on that so that another person doesn't work on the same function.
- Note that whoever comments about what they will add, other people should avoid working on that, until that person says otherwise.
- you can use third-party libraries if it can not be done with Python from scratch easily.
- just need to `add your own code` and update the `config.json` file,
- I have added one first function and conversation, so use that as your reference.


Happy Coding!!

### Please follow the below guidelines.
1. folder name must be `convert_{ext1}_to_{ext2}` (ex: `convert_srt_to_lrc`) #btw both are lyrics files extensions
2.  add a script with the same name as the folder name.
3. ~~add `__init__.py` inside the same folder.~~
4. write your code using `OOP` for beginners if they don't know that, you can simply write a function also no worries as long as that works :). if it's OOP based then main method will be according to first point. and for funtion the name will be according to first point.
5. after writing modify the config.yml file, to add your function in the main script, that's it, I have already configured the `convert_me.py` script, so no need to modify anything.
6. currently all the functions will take only two arguments, `input_file_path` and `output_file_path`, but if you want to add more, you might need to modify the code in the `convert_me.py` file
7. that's it, Check the README.md file in the folder `convert_srt_to_lrc`, you can add your GitHub username there. under **Features** section.
