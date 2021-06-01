# Human_deep_detection

## Introduction

이번 프로젝트는 deepface 라이브러리를 이용하여 사람의 감정과 성별, 인종을 감지하는 것을 목표로 했습니다.

---


## Dependencies

- Python 3, OpenCV, deepface
- To install the required packages, run pip install -r requirements.txt.

---


## Problem 

- AttributeError: module 'keras.utils.generic_utils' has no attribute 'populate_dict_with_module_objects' 
- AttributeError: module 'keras.utils.generic_utils' has no attribute 'to_snake_case' 


## Solve 

-  https://github.com/tensorflow/tensorflow/blob/master/tensorflow/python/keras/utils/generic_utils.py 
-  위의 코드에서 해당 함수를 찾아 직접 넣어주는 것으로 해결 하였습니다.

---


## Example Output

![result](/result1.png)

---


## References
https://pypi.org/project/deepface/

--- 

