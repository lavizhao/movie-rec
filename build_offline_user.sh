#

#生成用户feature，这里面用到了一个很好玩的特性，yeah， 不告诉你


echo hello

src_dir=$1
run_dir=./run_lib/
target_dir=./data/

#这是个例子
rm $target_dir/ufeature*

python $run_dir/gen_basic_feature.py $target_dir/user_info.jsons > $target_dir/ufeature1.txt

python $run_dir/collect_user_features.py $target_dir > $target_dir/raw_feature.txt
