# Name:     test.py
# Author:   Timothy Josh Agda
# Attempts to improve contrast to images and then scores them
# based on the Universal Image Quality Index

from sewar.full_ref import uqi
import imageIO as io
import imhist_lib as hist
import glob, os

def main():
    ScoreFile = open("scores.txt", "w")

    currentDir = os.getcwd()
    os.chdir("./original_images")

    allPics = glob.glob("*.jpg")
    allPics.extend(glob.glob("*.jpeg"))
    allPics.extend(glob.glob("*.png"))

    for file in allPics:
        print("Enhancing %s..." % file)

        # Read main image
        Img = io.imread_gray(file)
        # GroundTruthImg = io.imread_gray("eg2_grndtruth.jpg")  # [only for eg2_* images]

        # Run various histogram transformations
        ImgEq = hist.histeq(Img)[0]
        ImgBiEq = hist.histeqBI(Img)[0]
        ImgHyper = hist.histhyper(Img)
        ImgClahe = hist.histClahe(Img)

        # Save enhanced images
        io.imwrite_gray(currentDir + "/enhanced_images/%s_eq.png" % file[:-4], ImgEq)
        io.imwrite_gray(currentDir + "/enhanced_images/%s_biEq.png" % file[:-4], ImgBiEq)
        io.imwrite_gray(currentDir + "/enhanced_images/%s_hyper.png" % file[:-4], ImgHyper)
        io.imwrite_gray(currentDir + "/enhanced_images/%s_clahe.png" % file[:-4], ImgClahe)

        # Evaluate UQI scores compared to ground truth [only for eg2_* images]
        # ScoreEq = uqi(GroundTruthImg, ImgEq)
        # ScoreBiEq = uqi(GroundTruthImg, ImgBiEq)
        # ScoreHyper = uqi(GroundTruthImg, ImgHyper)
        # ScoreClahe = uqi(GroundTruthImg, ImgClahe)

        # Write to scores file [only for eg2_* images]
        # ScoreFile.write("%s\r\n" % file)
        # ScoreFile.write("Regular Equalization:\t\t%f\r\n" % ScoreEq)
        # ScoreFile.write("Bi-Histogram Equalization:\t%f\r\n" % ScoreBiEq)
        # ScoreFile.write("Histogram Hypoerbolization:\t%f\r\n" % ScoreHyper)
        # ScoreFile.write("CLAHE:\t\t\t\t\t\t%f\r\n\r\n" % ScoreClahe)

    ScoreFile.close()

if __name__ == "__main__":
    main()
