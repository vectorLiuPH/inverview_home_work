# 1. brief

A project base on `selenium` and `pytest` , is used to develop automation test scripts for MyObservatory.

Test cases:
```
1.Check situation general text displayed is equal with api response
2.Scroll screen to collect each days weather infomation in 9-day \-forecast and compare it to api response
```

# 2. project

```
├── README.md
├── src
   ├── testcases
   │     ├── test_xxx.py    # test cases depend on test steps 
   └── pages
         └── xxxpage
               └── locators.py    # page objects
               └── actions.py     # every test step`s code implement
          ├── api.py                    # calling api
          ├── tools.py                  # tools functions
          └── conftest.py               
```

# 3. How to use

### 3.1 Make sure you have python environment in your machine.
### 3.2 Run 'pip install -r requirements.txt' under project directory.
### 3.3 Please set your MyObservatory app in English language. (Simple Chinese and Traditional Chinese assertion is not finish yet.)
### 3.4 
#### 3.4.1 If you are the first time to start MyObservatory, please run below command under project/src:
```
pytest noReset=false -rerun=2
```
#### 3.4.2 If you are not the first time to start MyObservatory and already have agreed every permissions, please run below command:
```
pytest -rerun=2
```

