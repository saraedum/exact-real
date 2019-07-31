# Header file `cppyy.hpp`

``` cpp
namespace exactreal
{
    std::ostream& operator<<(std::ostream&, exactreal::Arb const&);
    std::ostream& operator<<(std::ostream&, exactreal::Arf const&);
    std::ostream& operator<<(std::ostream&, exactreal::RealNumber const&);
    template <typename Ring>
    std::ostream& operator<<(std::ostream&, exactreal::Module<Ring> const&);
    template <typename Ring>
    std::ostream& operator<<(std::ostream&, exactreal::Element<Ring> const&);
}
namespace exactreal
{
    exactreal::Arb binary(exactreal::Arb const& left, exactreal::Arb const& right, char op, exactreal::prec prec);
    exactreal::Arf binary(exactreal::Arf const& left, exactreal::Arf const& right, char op, exactreal::prec prec, Arf::Round round);
    template <typename T>
    T minus(T const& lhs);
    template <typename S, typename T, char op>
    auto boost_binary(S const& lhs, T const& rhs);
}
```
