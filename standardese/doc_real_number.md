# Header file `real_number.hpp`

``` cpp
namespace exactreal
{
    class RealNumber;
    template <typename Integer>
    std::enable_if_t<std::is_integral_v<Integer>, bool> RealNumber::operator<(Integer rhs) const noexcept;
    template <typename Integer>
    std::enable_if_t<std::is_integral_v<Integer>, bool> RealNumber::operator>(Integer rhs) const noexcept;
    template <typename Integer>
    std::enable_if_t<std::is_integral_v<Integer>, bool> RealNumber::operator==(Integer rhs) const noexcept;
}
```
