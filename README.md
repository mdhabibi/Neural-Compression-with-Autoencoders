# CompressNetMNIST




## Model Analysis and Comparison

In this project, we evaluated four different autoencoder models on the EMNIST dataset, focusing on their performance in terms of training and validation loss, Mean Squared Error (MSE), Structural Similarity Index (SSIM), and Peak Signal-to-Noise Ratio (PSNR). The following is a detailed analysis of each model's performance:

### Model 01:
- **Training Loss:** 0.00379
- **Validation Loss:** 0.00401
- **MSE:** 0.00317 (both Autoencoder and Decoder)
- **SSIM:** 0.98057 (both Autoencoder and Decoder)
- **PSNR:** 26.02 dB (both Autoencoder and Decoder)

Model 01 demonstrates the best overall performance with the lowest training and validation loss, indicating excellent generalization. It also achieved the highest SSIM, reflecting superior image reconstruction quality.

### Model 02:
- **Training Loss:** 0.01034
- **Validation Loss:** 0.01121
- **MSE:** 0.01106 (both Autoencoder and Decoder)
- **SSIM:** 0.92342 (both Autoencoder and Decoder)
- **PSNR:** 20.26 dB (both Autoencoder and Decoder)

Model 02 shows a higher training and validation loss, suggesting potential overfitting. The lower SSIM and PSNR indicate a comparatively reduced ability in preserving image details during reconstruction.

### Model 03:
- **Training Loss:** 0.00390
- **Validation Loss:** 0.00421
- **MSE:** 0.00371 (both Autoencoder and Decoder)
- **SSIM:** 0.97389 (both Autoencoder and Decoder)
- **PSNR:** 24.85 dB (both Autoencoder and Decoder)

Model 03 offers a good balance between training and validation performance. It shows a high degree of image reconstruction accuracy, as evident from its SSIM and PSNR values.

### Model 04:
- **Training Loss:** 0.00506
- **Validation Loss:** 0.00533
- **MSE:** 0.00468 (both Autoencoder and Decoder)
- **SSIM:** 0.96943 (both Autoencoder and Decoder)
- **PSNR:** 23.90 dB (both Autoencoder and Decoder)

Model 04 falls between Models 01 and 02 in terms of performance metrics. It displays a moderate level of image reconstruction capability, reflected in its SSIM and PSNR scores.

### Summary
The evaluation metrics indicate that **Model 01** stands out as the most effective in reconstructing images from the EMNIST dataset, with the highest SSIM and PSNR scores and the lowest loss values. Models 03 and 04 offer competitive performance, with Model 02 lagging slightly behind in terms of image quality preservation. These insights are crucial for further refinement of autoencoder models for image reconstruction tasks.


The results show that the **Mean Squared Error (MSE)** is identical for both the full autoencoder
and the separate encoder and decoder models. This indicates a consistent level of performance
in terms of reconstruction error, whether we're using the combined autoencoder model
or the individual encoder and decoder in sequence. An MSE of around **0.004** suggests that,
on average, the squared difference between the original and reconstructed pixels is quite low,
which is typically a good sign in terms of reconstruction quality.

The **SSIM (Structural Similarity Index)** results indicate a high degree of similarity
between the original images and the reconstructed images, both for the full autoencoder
and the decoder setup. An SSIM value close to 1, like the ones my model is getting **(0.976)**,
suggests that the reconstructed images are very close to the original images in terms of
structural integrity, brightness, and contrast.

These high SSIM values are a good sign and imply that my autoencoder and its individual
components (encoder and decoder) are effectively capturing and reconstructing the important
features of the input images. This is particularly encouraging because SSIM is often considered
a more perceptually relevant metric compared to MSE, as it aligns more closely with human
visual perception.

The **PSNR (Peak Signal-to-Noise Ratio)** values I've obtained for both the full autoencoder
and the decoder setup are identical, indicating a consistent level of performance in terms of
image reconstruction quality. A PSNR of around **24.47 dB** is generally considered a good result,
especially for lossy compression techniques like autoencoders.

## Interpretation:

1. **Consistency Across Metrics:** The fact that both the MSE and SSIM metrics, as well as PSNR,
show similar results for the full autoencoder and the decoder setup suggests that both components
of my model are effectively working together to reconstruct the images with a high degree of fidelity.

2. **PSNR Value:** PSNR values in the range of **20-30 dB** are often seen in image compression scenarios.
The exact 'good' value can depend on the specific application and the nature of the images.
In many cases, a PSNR above **30 dB** is considered excellent, but for complex datasets
or more challenging reconstruction tasks, a PSNR in the **mid-20s** can still be quite good.

3. **Overall Model Performance:** These results indicate that my autoencoder is performing well
in reconstructing the images. It's capturing enough detail and structural information to maintain
a high level of similarity to the original images.








