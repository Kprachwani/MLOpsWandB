import wandb

wandb.init(project="mlops-course-project")

wandb.log({
    "accuracy": 0.8,
    "loss": 0.5
})

wandb.finish()
