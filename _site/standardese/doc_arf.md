# Header file `arf.hpp`

``` cpp
namespace exactreal
{
    namespace yap
    {
        template <typename T>
        using isArf = std::is_same<Arf, T>;
    }
    template <typename T, typename U>
    constexpr ::boost::yap::detail::udt_any_binary_op_result_t<yap::ArfExpr, ::boost::yap::expr_kind::multiplies, T, U, yap::isArf> operator*(T&& lhs, U&& rhs);
    template <typename T, typename U>
    constexpr ::boost::yap::detail::udt_any_binary_op_result_t<yap::ArfExpr, ::boost::yap::expr_kind::plus, T, U, yap::isArf> operator+(T&& lhs, U&& rhs);
    template <typename T, typename U>
    constexpr ::boost::yap::detail::udt_any_binary_op_result_t<yap::ArfExpr, ::boost::yap::expr_kind::minus, T, U, yap::isArf> operator-(T&& lhs, U&& rhs);
    template <typename T, typename U>
    constexpr ::boost::yap::detail::udt_any_binary_op_result_t<yap::ArfExpr, ::boost::yap::expr_kind::divides, T, U, yap::isArf> operator/(T&& lhs, U&& rhs);
    template <typename T>
    constexpr ::boost::yap::detail::udt_unary_op_result_t<yap::ArfExpr, ::boost::yap::expr_kind::negate, T, yap::isArf> operator-(T&& x);
    template <::boost::yap::expr_kind Kind, typename Tuple, typename Expr>
    constexpr auto operator+(yap::ArfExpr<Kind, Tuple> const& lhs, Expr&& rhs);
    template <::boost::yap::expr_kind Kind, typename Tuple, typename Expr>
    constexpr auto operator+(yap::ArfExpr<Kind, Tuple>& lhs, Expr&& rhs);
    template <::boost::yap::expr_kind Kind, typename Tuple, typename Expr>
    constexpr auto operator+(yap::ArfExpr<Kind, Tuple>&& lhs, Expr&& rhs);
    template <typename T, ::boost::yap::expr_kind Kind, typename Tuple>
    constexpr ::boost::yap::detail::free_binary_op_result_t<yap::ArfExpr, ::boost::yap::expr_kind::plus, T, yap::ArfExpr<Kind, Tuple> &&> operator+(T&& lhs, yap::ArfExpr<Kind, Tuple>&& rhs);
    template <typename T, ::boost::yap::expr_kind Kind, typename Tuple>
    constexpr ::boost::yap::detail::free_binary_op_result_t<yap::ArfExpr, ::boost::yap::expr_kind::plus, T, const yap::ArfExpr<Kind, Tuple> &> operator+(T&& lhs, yap::ArfExpr<Kind, Tuple> const& rhs);
    template <typename T, ::boost::yap::expr_kind Kind, typename Tuple>
    constexpr ::boost::yap::detail::free_binary_op_result_t<yap::ArfExpr, ::boost::yap::expr_kind::plus, T, yap::ArfExpr<Kind, Tuple> &> operator+(T&& lhs, yap::ArfExpr<Kind, Tuple>& rhs);
    template <::boost::yap::expr_kind Kind, typename Tuple, typename Expr>
    constexpr auto operator-(yap::ArfExpr<Kind, Tuple> const& lhs, Expr&& rhs);
    template <::boost::yap::expr_kind Kind, typename Tuple, typename Expr>
    constexpr auto operator-(yap::ArfExpr<Kind, Tuple>& lhs, Expr&& rhs);
    template <::boost::yap::expr_kind Kind, typename Tuple, typename Expr>
    constexpr auto operator-(yap::ArfExpr<Kind, Tuple>&& lhs, Expr&& rhs);
    template <typename T, ::boost::yap::expr_kind Kind, typename Tuple>
    constexpr ::boost::yap::detail::free_binary_op_result_t<yap::ArfExpr, ::boost::yap::expr_kind::minus, T, yap::ArfExpr<Kind, Tuple> &&> operator-(T&& lhs, yap::ArfExpr<Kind, Tuple>&& rhs);
    template <typename T, ::boost::yap::expr_kind Kind, typename Tuple>
    constexpr ::boost::yap::detail::free_binary_op_result_t<yap::ArfExpr, ::boost::yap::expr_kind::minus, T, const yap::ArfExpr<Kind, Tuple> &> operator-(T&& lhs, yap::ArfExpr<Kind, Tuple> const& rhs);
    template <typename T, ::boost::yap::expr_kind Kind, typename Tuple>
    constexpr ::boost::yap::detail::free_binary_op_result_t<yap::ArfExpr, ::boost::yap::expr_kind::minus, T, yap::ArfExpr<Kind, Tuple> &> operator-(T&& lhs, yap::ArfExpr<Kind, Tuple>& rhs);
    template <::boost::yap::expr_kind Kind, typename Tuple, typename Expr>
    constexpr auto operator*(yap::ArfExpr<Kind, Tuple> const& lhs, Expr&& rhs);
    template <::boost::yap::expr_kind Kind, typename Tuple, typename Expr>
    constexpr auto operator*(yap::ArfExpr<Kind, Tuple>& lhs, Expr&& rhs);
    template <::boost::yap::expr_kind Kind, typename Tuple, typename Expr>
    constexpr auto operator*(yap::ArfExpr<Kind, Tuple>&& lhs, Expr&& rhs);
    template <typename T, ::boost::yap::expr_kind Kind, typename Tuple>
    constexpr ::boost::yap::detail::free_binary_op_result_t<yap::ArfExpr, ::boost::yap::expr_kind::multiplies, T, yap::ArfExpr<Kind, Tuple> &&> operator*(T&& lhs, yap::ArfExpr<Kind, Tuple>&& rhs);
    template <typename T, ::boost::yap::expr_kind Kind, typename Tuple>
    constexpr ::boost::yap::detail::free_binary_op_result_t<yap::ArfExpr, ::boost::yap::expr_kind::multiplies, T, const yap::ArfExpr<Kind, Tuple> &> operator*(T&& lhs, yap::ArfExpr<Kind, Tuple> const& rhs);
    template <typename T, ::boost::yap::expr_kind Kind, typename Tuple>
    constexpr ::boost::yap::detail::free_binary_op_result_t<yap::ArfExpr, ::boost::yap::expr_kind::multiplies, T, yap::ArfExpr<Kind, Tuple> &> operator*(T&& lhs, yap::ArfExpr<Kind, Tuple>& rhs);
    template <::boost::yap::expr_kind Kind, typename Tuple, typename Expr>
    constexpr auto operator/(yap::ArfExpr<Kind, Tuple> const& lhs, Expr&& rhs);
    template <::boost::yap::expr_kind Kind, typename Tuple, typename Expr>
    constexpr auto operator/(yap::ArfExpr<Kind, Tuple>& lhs, Expr&& rhs);
    template <::boost::yap::expr_kind Kind, typename Tuple, typename Expr>
    constexpr auto operator/(yap::ArfExpr<Kind, Tuple>&& lhs, Expr&& rhs);
    template <typename T, ::boost::yap::expr_kind Kind, typename Tuple>
    constexpr ::boost::yap::detail::free_binary_op_result_t<yap::ArfExpr, ::boost::yap::expr_kind::divides, T, yap::ArfExpr<Kind, Tuple> &&> operator/(T&& lhs, yap::ArfExpr<Kind, Tuple>&& rhs);
    template <typename T, ::boost::yap::expr_kind Kind, typename Tuple>
    constexpr ::boost::yap::detail::free_binary_op_result_t<yap::ArfExpr, ::boost::yap::expr_kind::divides, T, const yap::ArfExpr<Kind, Tuple> &> operator/(T&& lhs, yap::ArfExpr<Kind, Tuple> const& rhs);
    template <typename T, ::boost::yap::expr_kind Kind, typename Tuple>
    constexpr ::boost::yap::detail::free_binary_op_result_t<yap::ArfExpr, ::boost::yap::expr_kind::divides, T, yap::ArfExpr<Kind, Tuple> &> operator/(T&& lhs, yap::ArfExpr<Kind, Tuple>& rhs);
    template <::boost::yap::expr_kind Kind, typename Tuple>
    auto operator-(yap::ArfExpr<Kind, Tuple> const& x);
    template <::boost::yap::expr_kind Kind, typename Tuple>
    auto operator-(yap::ArfExpr<Kind, Tuple>& x);
    template <::boost::yap::expr_kind Kind, typename Tuple>
    auto operator-(yap::ArfExpr<Kind, Tuple>&& x);
    template <boost::yap::expr_kind Kind, typename Tuple>
    Arf::Arf(yap::ArfExpr<Kind, Tuple> const& expr) noexcept;
    template <boost::yap::expr_kind Kind, typename Tuple>
    Arf::Arf(yap::ArfExpr<Kind, Tuple>&& expr) noexcept;
    template <boost::yap::expr_kind Kind, typename Tuple>
    exactreal::Arf& Arf::operator=(yap::ArfExpr<Kind, Tuple> const& expr) noexcept;
    template <boost::yap::expr_kind Kind, typename Tuple, typename Lambda>
    exactreal::Arf& inplace_binop(exactreal::Arf& self, yap::ArfExpr<Kind, Tuple> const& expr, Lambda op) noexcept;
    template <typename ... Args>
    auto Arf::operator()(Args &&... args) const noexcept;
}
```
