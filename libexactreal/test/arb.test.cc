/**********************************************************************
 *  This file is part of exact-real.
 *
 *        Copyright (C) 2019 Vincent Delecroix
 *        Copyright (C) 2019 Julian Rüth
 *
 *  exact-real is free software: you can redistribute it and/or modify
 *  it under the terms of the GNU General Public License as published by
 *  the Free Software Foundation, either version 3 of the License, or
 *  (at your option) any later version.
 *
 *  exact-real is distributed in the hope that it will be useful,
 *  but WITHOUT ANY WARRANTY; without even the implied warranty of
 *  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 *  GNU General Public License for more details.
 *
 *  You should have received a copy of the GNU General Public License
 *  along with exact-real. If not, see <https://www.gnu.org/licenses/>.
 *********************************************************************/

#include <boost/lexical_cast.hpp>

#include "../exact-real/arb.hpp"
#include "external/catch2/single_include/catch2/catch.hpp"

using boost::lexical_cast;
using std::string;

namespace exactreal::test {

TEST_CASE("Create/Destroy Arb", "[arb]") {
  delete new Arb();
}

TEST_CASE("Relational Operators of Arb", "[arb]") {
  Arb x(-1), y(1);

  REQUIRE(((x < y) && *(x < y)));
  REQUIRE(((y > x) && *(y > x)));
  REQUIRE(((x <= y) && *(x <= y)));
  REQUIRE(((y >= x) && *(y >= x)));
  REQUIRE(((x == x) && *(x == x)));
  REQUIRE(((x != y) && *(x != y)));
  REQUIRE(((y > x) && !*(y < x)));
  REQUIRE(((x < y) && !*(x > y)));
  REQUIRE(((y >= x) && !*(y <= x)));
  REQUIRE(((x <= y) && !*(x >= y)));
}

TEST_CASE("Unary Minus of Arb", "[arb]") {
  Arb x(1);

  REQUIRE((x == -(-x) && *(x == -(-x))));
  REQUIRE((x == -x && !*(x == -x)));
}

TEST_CASE("Exactness of Arb", "[arb]") {
  REQUIRE(Arb(mpq_class(1, 2), 2).is_exact());
  REQUIRE(!Arb(mpq_class(1, 3), 2).is_exact());
}

TEST_CASE("Print Arb", "[arb]") {
  REQUIRE(lexical_cast<string>(Arb()) == "0");
  REQUIRE(lexical_cast<string>(Arb(1337)) == "1337.00");
  REQUIRE(lexical_cast<string>(Arb(string(1337, '1'), 1024)) == "[1.11111e+1336 +/- 1.12e+1330]");
  REQUIRE(lexical_cast<string>(Arb("." + string(1337, '0') + "1", 1024)) == "[1.00000e-1338 +/- 3e-1348]");
  REQUIRE(lexical_cast<string>(Arb(mpq_class(1, 2), 1)) == "0.500000");
  REQUIRE(lexical_cast<string>(Arb(mpq_class(1, 3), 64)) == "[0.333333 +/- 3.34e-7]");
}

TEST_CASE("Cast to Arf", "[arb][arf]") {
  Arb x(mpq_class(1, 2), 4);

  REQUIRE(static_cast<std::pair<Arf, Arf>>(x).first == Arf(.5));
  REQUIRE(static_cast<std::pair<Arf, Arf>>(x).second == Arf(.5));
}

TEST_CASE("Zero", "[arb][zero]") {
  Arb x = Arb::zero();

  REQUIRE(x == 0);
}

TEST_CASE("One", "[arb][one]") {
  Arb x = Arb::one();

  REQUIRE(x == 1);
}

TEST_CASE("Infinite Values", "[arb][inf]") {
  Arb x = Arb::pos_inf();
  Arb y = Arb::neg_inf();

  REQUIRE(*(x > 0));
  REQUIRE(*(y < 0));
}

TEST_CASE("Indeterminate Value", "[arb][indeterminate]") {
  Arb x = Arb::indeterminate();

  REQUIRE(!(x >= 0));
  REQUIRE(!(x <= 0));
}

}  // namespace exactreal::test
