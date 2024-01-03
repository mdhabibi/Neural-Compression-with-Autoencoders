# CompressNetMNIST
## Project Overview: Data Compression with Complex Autoencoder Architectures

The primary objective of this project is to develop an efficient model for data compression. The focus is on leveraging complex autoencoder architectures to achieve significant dimensionality reduction while minimizing information loss. These models are adept at encoding high-dimensional data into a lower-dimensional space, effectively compressing the data while preserving its essential characteristics. 
This approach aims to reduce the memory footprint of data, which is crucial in various applications, including storage optimization and efficient data transmission. It's important to note that this form of compression primarily pertains to reducing dimensionality and memory usage, rather than decreasing storage size.

## Autoencoder Architecture and Applications
<div align="center">
  <img src="images/Autoencoder_schema.png" width="400">
</div>
*By Michela Massi - Own work, CC BY-SA 4.0, https://commons.wikimedia.org/w/index.php?curid=80177333*


Autoencoders are a type of neural network architecture used for unsupervised learning. They are designed to encode input data into a lower-dimensional representation and then reconstruct the original data from this representation. This process allows for learning efficient data codings in an automated fashion.

### Applications of Autoencoders:
- **Data Compression:** In the context of data compression, autoencoders excel at representing data in a more compact form, which helps in reducing memory usage without significantly compromising the data's integrity.
- **Dimensionality Reduction:** Autoencoders can reduce the dimensionality of data, similar to Principal Component Analysis (PCA), making them useful for data visualization and noise reduction.
- **Feature Learning, Image Reconstruction, and Generative Models:** They are also used for automated feature learning, image reconstruction tasks like denoising and inpainting, and as generative models for creating new data instances.


### Design Choices for Encoder and Decoder:
For high-quality image reconstruction, I made specific design choices in the encoder and decoder parts of the autoencoder:

#### Encoder - I opted for `Conv2D` layers with strides instead of `MaxPooling2D` to:

- **Preservation of Spatial Information:** By using only `Conv2D` layers with strides for downsampling, I aimed to preserve more spatial information compared to max pooling. Strided convolutions reduce dimensions while learning how to downsample, retaining more details that are crucial for accurate reconstruction.
- **Balancing Efficiency and Detail:** I avoided `MaxPooling2D` to minimize information loss and ensure that the encoded representation retains sufficient detail for high-quality reconstruction.

#### Decoder - Conv2DTranspose over UpSampling:
- **Quality of Reconstruction:** To reconstruct the images from the latent representation, I chose `Conv2DTranspose` layers over `UpSampling2D`. This decision was driven by the need for higher-quality image reconstruction.
- **Learnable Upsampling:** `Conv2DTranspose` layers offer learnable parameters for upsampling, allowing the network to effectively learn how to expand the encoded representation back to the original image size.
- **Avoiding Artifacts:** The use of `Conv2DTranspose` also helps in reducing artifacts that might occur with simpler upsampling methods.

### Experimental Approach:
To determine the optimal layer configuration for the decoder, I tested four different models, each with a unique decoder structure. The performance of each model was assessed based on several key metrics. This evaluation was conducted for both the full autoencoder models and only their decoder parts, to gauge their respective abilities in reconstructing images accurately.
This systematic exploration helps us understand the impact of decoder configurations on image reconstruction quality, providing insights for enhancing autoencoder performance in data compression tasks. 

### Dataset Used:
For this analysis, the EMNIST-Balanced dataset was chosen. It is a comprehensive dataset that includes a mix of digits, uppercase, and lowercase letters, offering a diverse range of characters for my models to learn and reconstruct.

- Below is a detailed analysis including explanations of each metric:

### Metrics Explained:
- **Training Loss:** Measures how well the model is performing during the training phase. Lower values indicate better performance.
- **Validation Loss:** Indicates the model's performance on unseen data. It helps to identify overfitting.
- **Mean Squared Error (MSE):** Quantifies the average squared difference between the reconstructed and original images. Lower MSE values signify more accurate reconstructions.
- **Structural Similarity Index (SSIM):** Assesses the perceived quality of the reconstructed image compared to the original. Ranges from -1 to 1, with higher values indicating better image quality.
- **Peak Signal-to-Noise Ratio (PSNR):** Measures the ratio between the maximum possible power of a signal and the power of corrupting noise. Expressed in decibels (dB), higher values represent better reconstruction quality.

<div align="center">
  <img src="images/autoencoder_model_comparisons.png" width="800">
</div>

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
### Conclusion:
This approach allowed us to systematically explore the impact of different decoder configurations on the quality of image reconstruction, leading to valuable insights for enhancing autoencoder performance in image-based tasks.



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








