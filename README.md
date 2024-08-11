# Object-Detection on custom dataset (YOLO v8)

If you want to train YOLO v8 on [Open Images v6 Dataset](https://storage.googleapis.com/openimages/web/factsfigures_v7.html), then do the following :

1. Create a Project folder. All downloads should be in this folder.
2. Download the Open Images Labels : [train](https://storage.googleapis.com/openimages/v6/oidv6-train-annotations-bbox.csv), [validation](https://storage.googleapis.com/openimages/v5/validation-annotations-bbox.csv), [test](https://storage.googleapis.com/openimages/v5/test-annotations-bbox.csv) and [class description](https://storage.googleapis.com/openimages/v7/oidv7-class-descriptions.csv) file.
3. Download and execute **compute_class_freq.py**. Select one or more classes of your choice from **class_descriptions.csv**.
4. Note the labelname of selected classes.
5. Download and execute **create_image_list_file.py** with appropriate class IDs.
6. Execute **create_dataset_yolo_format.py**
7. Download the [downloader_modified.py](https://raw.githubusercontent.com/raoashish2309/Object-Detection/main/util/downloader_modified.py) file and execute as :

       python3 downloader_modified.py $IMAGE_LIST_FILE 

8. Download **config.yaml** file and configure it.
9. Execute **setup.py** to organize utilities and create subfolders for I/O.
10. To train YOLO v8 model on the system execute **train.py** and use **predict.py** as :

        python3 predict.py --mode="image" --infilepath="input/filename.jpeg"

        python3 predict.py --mode="video" --infilepath="input/filename.mp4" --outfilepath=$DESTINATION_FOLDER

12. To train YOLO v8 model on google colab upload project folder with data, input, and ouput subfolders.
13. Reconfigure **config.yaml** as shown in **g_config.yaml**.
14. Run **g_train.ipynb** file with appropriate runtime type.
