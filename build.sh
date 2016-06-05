#!/bin/env sh

echo "开始build数据"

src_dir=$1
run_dir=./run_lib/
target_dir=./data/

#build 电影数据
python $run_dir/build_movie_data.py $1/tags.csv $1/movies.csv > $target_dir/movie_info.jsons

#build 用户数据
python $run_dir/build_user_data.py $1/ratings.csv $1/tags.csv > $target_dir/user_info.jsons


