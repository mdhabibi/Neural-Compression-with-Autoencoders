import matplotlib.pyplot as plt

# Data for the four models
models = {
    "model01": {
        "train_loss": 0.003792035859078169,
        "val_loss": 0.004013359546661377,
        "mse_autoencoder": 0.0031659754,
        "mse_decoder": 0.0031659754,
        "ssim_autoencoder": 0.9805696272187762,
        "ssim_decoder": 0.9805696272187762,
        "psnr_autoencoder": 26.021341569896215,
        "psnr_decoder": 26.021341569896215
    },
    "model02": {
        "train_loss": 0.010338369756937027,
        "val_loss": 0.011210279539227486,
        "mse_autoencoder": 0.011063212,
        "mse_decoder": 0.011063212,
        "ssim_autoencoder": 0.9234211692379581,
        "ssim_decoder": 0.9234211692379581,
        "psnr_autoencoder": 20.25646765483872,
        "psnr_decoder": 20.25646765483872
    },
    "model03": {
        "train_loss": 0.003903726814314723,
        "val_loss": 0.004210158251225948,
        "mse_autoencoder": 0.0037133987,
        "mse_decoder": 0.0037133987,
        "ssim_autoencoder": 0.9738876712726958,
        "ssim_decoder": 0.9738876712726958,
        "psnr_autoencoder": 24.848811575055276,
        "psnr_decoder": 24.848811575055276
    },
    "model04": {
        "train_loss": 0.0050644357688724995,
        "val_loss": 0.005331302061676979,
        "mse_autoencoder": 0.0046826783,
        "mse_decoder": 0.0046826783,
        "ssim_autoencoder": 0.9694286496918878,
        "ssim_decoder": 0.9694286496918878,
        "psnr_autoencoder": 23.9010523576152,
        "psnr_decoder": 23.9010523576152
    }
}

# Colors for each model
colors = ['b', 'g', 'r', 'c']

# Plotting
fig, axs = plt.subplots(2, 2, figsize=(12, 10))

# Training and Validation Loss
for i, (model, color) in enumerate(zip(models, colors)):
    axs[0, 0].scatter(['Train', 'Validation'], [models[model]['train_loss'], models[model]['val_loss']], color=color, label=model)
axs[0, 0].set_title('Training and Validation Loss')
axs[0, 0].legend()

# MSE
for i, (model, color) in enumerate(zip(models, colors)):
    axs[0, 1].scatter(['Autoencoder', 'Decoder'], [models[model]['mse_autoencoder'], models[model]['mse_decoder']], color=color, label=model)
axs[0, 1].set_title('MSE Comparison')
axs[0, 1].legend()

# SSIM
for i, (model, color) in enumerate(zip(models, colors)):
    axs[1, 0].scatter(['Autoencoder', 'Decoder'], [models[model]['ssim_autoencoder'], models[model]['ssim_decoder']], color=color, label=model)
axs[1, 0].set_title('SSIM Comparison')
axs[1, 0].legend()

# PSNR
for i, (model, color) in enumerate(zip(models, colors)):
    axs[1, 1].scatter(['Autoencoder', 'Decoder'], [models[model]['psnr_autoencoder'], models[model]['psnr_decoder']], color=color, label=model)
axs[1, 1].set_title('PSNR Comparison')
axs[1, 1].legend()

plt.tight_layout()

# Save the plot to a file
plt.savefig('/Volumes/D/GitHub-Portfolio/CompressNetMNIST/images/autoencoder_model_comparisons.png')
plt.show()

