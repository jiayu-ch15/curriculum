#!/bin/sh
ulimit -n 32768
env="MPE"
scenario="simple_spread"
num_landmarks=4
num_agents=4
algo="diversified_novelty_parentsampling_sp"
# algo='check_novelty_max'
seed_max=1

echo "env is ${env}, scenario is ${scenario}, algo is ${algo}, seed is ${seed_max}"

for seed in {2,3};
do
    echo "seed is ${seed}:"
    CUDA_VISIBLE_DEVICES=2 python train_mpe_curriculum_sp.py --env_name ${env} --algorithm_name ${algo} --scenario_name ${scenario} --num_agents ${num_agents} --num_landmarks ${num_landmarks} --seed ${seed} --n_rollout_threads 500 --num_mini_batch 2 --episode_length 70 --num_env_steps 40000000 --ppo_epoch 15 --recurrent_policy --use_popart --use-max-grad-norm
    echo "training is done!"
done
# seed=3
# CUDA_VISIBLE_DEVICES=0 python train_mpe_curriculum_sp.py --env_name ${env} --algorithm_name ${algo} --scenario_name ${scenario} --num_agents ${num_agents} --num_landmarks ${num_landmarks} --seed ${seed} --n_rollout_threads 500 --num_mini_batch 2 --episode_length 70 --num_env_steps 60000000 --ppo_epoch 15 --recurrent_policy --use_popart --use-max-grad-norm
