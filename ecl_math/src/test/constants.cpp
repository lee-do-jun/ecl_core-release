/**
 * @file /src/test/constants.cpp
 *
 * @brief Unit Test for the mathematical constants.
 *
 * @date May 2009
 **/

/*****************************************************************************
** Includes
*****************************************************************************/

#include <iostream>
#include <gtest/gtest.h>
#include "../../include/ecl/math/constants.hpp"

/*****************************************************************************
** Tests
*****************************************************************************/

TEST(MathTests,pi) {
	EXPECT_EQ(3.141592653589793238462643383279502884197169399375105820974944, ecl::pi);
	EXPECT_EQ(1.57079632679489661923,ecl::pi_2);
	EXPECT_EQ(0.78539816339744830962,ecl::pi_4);
}

/*****************************************************************************
** Main program
*****************************************************************************/

int main(int argc, char **argv) {

    testing::InitGoogleTest(&argc,argv);
    return RUN_ALL_TESTS();
}

