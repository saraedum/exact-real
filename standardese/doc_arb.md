# Header file `arb.hpp`

``` cpp
namespace exactreal
{
    namespace yap
    {
        using exactreal::Arb;
        template <typename T>
        using isArb = std::is_same<Arb, T>;
    }
    template <typename T, typename U>
    constexpr ::boost::yap::detail::udt_any_binary_op_result_t<yap::ArbExpr, ::boost::yap::expr_kind::multiplies, T, U, yap::isArb> operator*(T&& lhs, U&& rhs);
    template <typename T, typename U>
    constexpr ::boost::yap::detail::udt_any_binary_op_result_t<yap::ArbExpr, ::boost::yap::expr_kind::plus, T, U, yap::isArb> operator+(T&& lhs, U&& rhs);
    template <typename T, typename U>
    constexpr ::boost::yap::detail::udt_any_binary_op_result_t<yap::ArbExpr, ::boost::yap::expr_kind::minus, T, U, yap::isArb> operator-(T&& lhs, U&& rhs);
    template <typename T, typename U>
    constexpr ::boost::yap::detail::udt_any_binary_op_result_t<yap::ArbExpr, ::boost::yap::expr_kind::divides, T, U, yap::isArb> operator/(T&& lhs, U&& rhs);
    template <typename T>
    constexpr ::boost::yap::detail::udt_unary_op_result_t<yap::ArbExpr, ::boost::yap::expr_kind::negate, T, yap::isArb> operator-(T&& x);
    template <::boost::yap::expr_kind Kind, typename Tuple, typename Expr>
    constexpr auto operator+(yap::ArbExpr<Kind, Tuple> const& lhs, Expr&& rhs);
    template <::boost::yap::expr_kind Kind, typename Tuple, typename Expr>
    constexpr auto operator+(yap::ArbExpr<Kind, Tuple>& lhs, Expr&& rhs);
    template <::boost::yap::expr_kind Kind, typename Tuple, typename Expr>
    constexpr auto operator+(yap::ArbExpr<Kind, Tuple>&& lhs, Expr&& rhs);
    template <typename T, ::boost::yap::expr_kind Kind, typename Tuple>
    constexpr ::boost::yap::detail::free_binary_op_result_t<yap::ArbExpr, ::boost::yap::expr_kind::plus, T, yap::ArbExpr<Kind, Tuple> &&> operator+(T&& lhs, yap::ArbExpr<Kind, Tuple>&& rhs);
    template <typename T, ::boost::yap::expr_kind Kind, typename Tuple>
    constexpr ::boost::yap::detail::free_binary_op_result_t<yap::ArbExpr, ::boost::yap::expr_kind::plus, T, const yap::ArbExpr<Kind, Tuple> &> operator+(T&& lhs, yap::ArbExpr<Kind, Tuple> const& rhs);
    template <typename T, ::boost::yap::expr_kind Kind, typename Tuple>
    constexpr ::boost::yap::detail::free_binary_op_result_t<yap::ArbExpr, ::boost::yap::expr_kind::plus, T, yap::ArbExpr<Kind, Tuple> &> operator+(T&& lhs, yap::ArbExpr<Kind, Tuple>& rhs);
    template <::boost::yap::expr_kind Kind, typename Tuple, typename Expr>
    constexpr auto operator-(yap::ArbExpr<Kind, Tuple> const& lhs, Expr&& rhs);
    template <::boost::yap::expr_kind Kind, typename Tuple, typename Expr>
    constexpr auto operator-(yap::ArbExpr<Kind, Tuple>& lhs, Expr&& rhs);
    template <::boost::yap::expr_kind Kind, typename Tuple, typename Expr>
    constexpr auto operator-(yap::ArbExpr<Kind, Tuple>&& lhs, Expr&& rhs);
    template <typename T, ::boost::yap::expr_kind Kind, typename Tuple>
    constexpr ::boost::yap::detail::free_binary_op_result_t<yap::ArbExpr, ::boost::yap::expr_kind::minus, T, yap::ArbExpr<Kind, Tuple> &&> operator-(T&& lhs, yap::ArbExpr<Kind, Tuple>&& rhs);
    template <typename T, ::boost::yap::expr_kind Kind, typename Tuple>
    constexpr ::boost::yap::detail::free_binary_op_result_t<yap::ArbExpr, ::boost::yap::expr_kind::minus, T, const yap::ArbExpr<Kind, Tuple> &> operator-(T&& lhs, yap::ArbExpr<Kind, Tuple> const& rhs);
    template <typename T, ::boost::yap::expr_kind Kind, typename Tuple>
    constexpr ::boost::yap::detail::free_binary_op_result_t<yap::ArbExpr, ::boost::yap::expr_kind::minus, T, yap::ArbExpr<Kind, Tuple> &> operator-(T&& lhs, yap::ArbExpr<Kind, Tuple>& rhs);
    template <::boost::yap::expr_kind Kind, typename Tuple, typename Expr>
    constexpr auto operator*(yap::ArbExpr<Kind, Tuple> const& lhs, Expr&& rhs);
    template <::boost::yap::expr_kind Kind, typename Tuple, typename Expr>
    constexpr auto operator*(yap::ArbExpr<Kind, Tuple>& lhs, Expr&& rhs);
    template <::boost::yap::expr_kind Kind, typename Tuple, typename Expr>
    constexpr auto operator*(yap::ArbExpr<Kind, Tuple>&& lhs, Expr&& rhs);
    template <typename T, ::boost::yap::expr_kind Kind, typename Tuple>
    constexpr ::boost::yap::detail::free_binary_op_result_t<yap::ArbExpr, ::boost::yap::expr_kind::multiplies, T, yap::ArbExpr<Kind, Tuple> &&> operator*(T&& lhs, yap::ArbExpr<Kind, Tuple>&& rhs);
    template <typename T, ::boost::yap::expr_kind Kind, typename Tuple>
    constexpr ::boost::yap::detail::free_binary_op_result_t<yap::ArbExpr, ::boost::yap::expr_kind::multiplies, T, const yap::ArbExpr<Kind, Tuple> &> operator*(T&& lhs, yap::ArbExpr<Kind, Tuple> const& rhs);
    template <typename T, ::boost::yap::expr_kind Kind, typename Tuple>
    constexpr ::boost::yap::detail::free_binary_op_result_t<yap::ArbExpr, ::boost::yap::expr_kind::multiplies, T, yap::ArbExpr<Kind, Tuple> &> operator*(T&& lhs, yap::ArbExpr<Kind, Tuple>& rhs);
    template <::boost::yap::expr_kind Kind, typename Tuple, typename Expr>
    constexpr auto operator/(yap::ArbExpr<Kind, Tuple> const& lhs, Expr&& rhs);
    template <::boost::yap::expr_kind Kind, typename Tuple, typename Expr>
    constexpr auto operator/(yap::ArbExpr<Kind, Tuple>& lhs, Expr&& rhs);
    template <::boost::yap::expr_kind Kind, typename Tuple, typename Expr>
    constexpr auto operator/(yap::ArbExpr<Kind, Tuple>&& lhs, Expr&& rhs);
    template <typename T, ::boost::yap::expr_kind Kind, typename Tuple>
    constexpr ::boost::yap::detail::free_binary_op_result_t<yap::ArbExpr, ::boost::yap::expr_kind::divides, T, yap::ArbExpr<Kind, Tuple> &&> operator/(T&& lhs, yap::ArbExpr<Kind, Tuple>&& rhs);
    template <typename T, ::boost::yap::expr_kind Kind, typename Tuple>
    constexpr ::boost::yap::detail::free_binary_op_result_t<yap::ArbExpr, ::boost::yap::expr_kind::divides, T, const yap::ArbExpr<Kind, Tuple> &> operator/(T&& lhs, yap::ArbExpr<Kind, Tuple> const& rhs);
    template <typename T, ::boost::yap::expr_kind Kind, typename Tuple>
    constexpr ::boost::yap::detail::free_binary_op_result_t<yap::ArbExpr, ::boost::yap::expr_kind::divides, T, yap::ArbExpr<Kind, Tuple> &> operator/(T&& lhs, yap::ArbExpr<Kind, Tuple>& rhs);
    template <::boost::yap::expr_kind Kind, typename Tuple>
    auto operator-(yap::ArbExpr<Kind, Tuple> const& x);
    template <::boost::yap::expr_kind Kind, typename Tuple>
    auto operator-(yap::ArbExpr<Kind, Tuple>& x);
    template <::boost::yap::expr_kind Kind, typename Tuple>
    auto operator-(yap::ArbExpr<Kind, Tuple>&& x);
    template <boost::yap::expr_kind Kind, typename Tuple>
    Arb::Arb(yap::ArbExpr<Kind, Tuple> const& expr) noexcept;
    template <boost::yap::expr_kind Kind, typename Tuple>
    Arb::Arb(yap::ArbExpr<Kind, Tuple>&& expr) noexcept;
    template <boost::yap::expr_kind Kind, typename Tuple>
    exactreal::Arb& Arb::operator=(yap::ArbExpr<Kind, Tuple> const& expr) noexcept;
    template <boost::yap::expr_kind Kind, typename Tuple, typename Lambda>
    exactreal::Arb& inplace_binop(exactreal::Arb& self, yap::ArbExpr<Kind, Tuple> const& expr, Lambda op) noexcept;
    template <typename ... Args>
    auto Arb::operator()(Args &&... args) const noexcept;
}
```
