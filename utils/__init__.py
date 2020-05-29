from matplotlib import pyplot as plt


def draw_image(origina_image, modified_img, modified_title):
    plt.figure(figsize=(50, 50))

    plt.subplot(1, 2, 1)
    plt.imshow(origina_image, cmap='gray', vmin=0, vmax=255)
    plt.title('Original')

    plt.subplot(1, 2, 2)
    plt.imshow(modified_img, cmap='gray', vmin=0, vmax=255)
    plt.title(modified_title)

    plt.show()