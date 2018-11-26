#Label and move images for training
#from source folders into target folder and create update labels files as needed.


#Usage example
python label_move_data.py --image_src_dir=/Data-Engineering/data_src --image_target_dir=/Data-Engineering/data_output/images/all-labels --labels_dir=/Data-Engineering/data_output/images_label

#image_src_dir should have a structure as follow
`
+-color1
 |--model1
   |---image_file
 |--model2
   |---image_file
+-color2

`
