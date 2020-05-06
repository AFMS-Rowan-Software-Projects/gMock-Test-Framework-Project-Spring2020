#include <iostream>
#include <gtest/gtest.h>
#include "Polygon.h"
#include <unistd.h>



TEST(Polygon, getArea0) {
        // Arrange


        // Act


        // Assert
        usleep(3000000);
        ASSERT_EQ(1,1);


}

TEST(Polygon, getHeight1) {
        // Arrange


        // Act


        // Assert


}

TEST(Polygon, setHeight2) {
        // Arrange


        // Act


        // Assert


}

TEST(Polygon, getWidth3) {
        // Arrange


        // Act


        // Assert


}

TEST(Polygon, setWidth4) {
        // Arrange


        // Act


        // Assert


}

int main(int argc, char **argv) {
        testing::InitGoogleTest(&argc, argv);
        return RUN_ALL_TESTS();
}
