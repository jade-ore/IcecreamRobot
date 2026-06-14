#include <iostream>
#include <opencv2/opencv.hpp>
#include <pybind11/pybind11.hpp>

int main() {
    
    cv::Mat img = cv::imread("../../picture.jpeg");
    cv::Mat compressed;
    
    cv::Size target_size(15, 15);

    cv::resize(img, compressed, target_size, 0, 0);
    
    std::cout << cv::imwrite("squished.jpg", compressed) << std::endl;

    return 0;
}