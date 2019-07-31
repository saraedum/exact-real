# Header file `exact-real.hpp`

``` cpp
namespace exactreal
{
    using prec = mp_limb_signed_t;
    using size = prec;
    template <auto = 0>constexpr bool false_v = false;
    template <typename = void>constexpr bool false_t = false;
}
```
