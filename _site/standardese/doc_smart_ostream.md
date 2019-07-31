# Header file `smart_ostream.hpp`

``` cpp
namespace exactreal
{
    template <class T>
    std::ostream& operator<<(std::ostream& os, std::shared_ptr<T> const& self);
    template <class T>
    std::ostream& operator<<(std::ostream& os, std::unique_ptr<T> const& self);
}
```
