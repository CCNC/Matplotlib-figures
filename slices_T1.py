import matplotlib.pyplot as plt
import matplotlib.cm as cm
import nibabel as nb
import numpy as np

def brain_slice_T1(nifti_location):
    
    T1_img = nb.load(nifti_location)
    T1_data = T1_img.get_data()
    
    T1_T = np.transpose(T1_data, [1, 2, 0])
    T1_T2 = np.transpose(T1_T, [1, 2, 0])

    ##transverse, sagittal, coronal
    fig, axes = plt.subplots(3,10, figsize=(34,20), facecolor='w', edgecolor='k')
    fig.subplots_adjust(hspace=0.1, wspace=0.000, left = 0.04, right = 0.99)
    axes = axes.ravel()

    slice_no_x = 80
    slice_no_y = 245
    slice_no_z = 40

    for i in range(10):
        ##Transverse
        axes[i].imshow(np.flipud(T1_T[:,slice_no_y,:]),cmap=cm.gray)
        axes[i].set_title('Slice number: {}'.format(slice_no_y),color='g',fontsize=20, fontweight="bold")
        axes[i].axis('off')

        ##Coronal
        axes[i+10].imshow(np.flipud(T1_T[slice_no_x,:,:]),cmap=cm.gray)
        axes[i+10].set_title('Slice number: {}'.format(slice_no_x),color='g', fontsize=20, fontweight="bold")
        axes[i+10].axis('off')

        ##Sagittal
        axes[i+20].imshow(np.flipud(T1_T2[:,slice_no_z,:]),cmap=cm.gray)
        axes[i+20].set_title('Slice number: {}'.format(slice_no_z),color='g',fontsize=20, fontweight="bold")
        axes[i+20].axis('off')

        fig.suptitle(str(nifti_location), fontsize = 45)

        slice_no_x += 15
        slice_no_y -= 12
        slice_no_z += 15

        text1 = 'L->R'
        text2 = 'P->A'
        text3 = 'I->S'
        text4 = '     L'
        text5 = 'R'
        plt.text(0, 0.3, text1, fontsize=30, transform=plt.gcf().transFigure, style='italic')
        plt.text(0, 0.59, text2, fontsize=30, transform=plt.gcf().transFigure, style='italic')
        plt.text(0, 0.85, text3, fontsize=30, transform=plt.gcf().transFigure, style='italic')
        plt.text(0, 0.24, text4, fontsize=30, transform=plt.gcf().transFigure, color='navy')
        plt.text(1, 0.24, text5, fontsize=30, transform=plt.gcf().transFigure, color='navy')
        plt.text(0, 0.5, text4, fontsize=30, transform=plt.gcf().transFigure, color='navy')
        plt.text(1, 0.5, text5, fontsize=30, transform=plt.gcf().transFigure, color='navy')
        plt.text(0, 0.74, text4, fontsize=30, transform=plt.gcf().transFigure, color='navy')
        plt.text(1, 0.74, text5, fontsize=30, transform=plt.gcf().transFigure, color='navy')

    ##x - 왼쪽/오른쪽 (R), y - 앞/뒤 (A), z -위/아래 (S)
    ##First voxel axis goes from left to Right;
    ##Second voxel axis goes from posterior to Anterior;
    ##Third voxel axis goes from inferior to Superior.
    
    return fig, axes
