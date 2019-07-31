# Header file `cereal.hpp`

``` cpp
#include "arb.hpp"
#include "arf.hpp"
#include "element.hpp"
#include "integer_ring.hpp"
#include "module.hpp"
#include "number_field.hpp"
#include "rational_field.hpp"
#include "real_number.hpp"
extern "C"
{
    int arb_load_str(arb_t res, char const* data);
    char* arb_dump_str(arb_t const x);
    int arf_load_str(arf_t res, char const* data);
    char* arf_dump_str(arf_t const x);
}
namespace exactreal
{
    template <typename T>
    struct CerealWrap;
    template <typename Archive>
    void save(Archive& archive, exactreal::Arb const& self);
    template <typename Archive>
    void load(Archive& archive, exactreal::Arb& self);
    template <typename Archive>
    void save(Archive& archive, exactreal::Arf const& self);
    template <typename Archive>
    void load(Archive& archive, exactreal::Arf& self);
    template <typename Archive, typename Ring>
    void save(Archive& archive, Element<Ring> const& self);
    template <typename Archive, typename Ring>
    void load(Archive& archive, Element<Ring>& self);
    template <typename Archive>
    void serialize(Archive&, exactreal::IntegerRing&);
    template <typename Archive>
    void serialize(Archive&, exactreal::RationalField&);
    template <typename Archive>
    void serialize(Archive& archive, exactreal::NumberField& self);
    struct RealNumberCereal;
    template <typename T, typename Cerealizer>
    struct ForwardingCereal;
    template <typename Archive>
    void save(Archive& archive, CerealWrap<mpq_class> const& self);
    template <typename Archive>
    void load(Archive& archive, CerealWrap<mpq_class>& self);
    template <typename Archive>
    void save(Archive& archive, CerealWrap<mpz_class> const& self);
    template <typename Archive>
    void load(Archive& archive, CerealWrap<mpz_class>& self);
    template <typename Archive, typename T>
    void save(Archive& archive, CerealWrap<T> const& self);
    template <typename Archive, typename T>
    void load(Archive& archive, CerealWrap<T>& self);
}
namespace cereal
{
    template <typename Archive>
    void save(Archive& archive, std::shared_ptr<const exactreal::RealNumber> const& self);
    template <typename Archive>
    void load(Archive& archive, std::shared_ptr<const exactreal::RealNumber>& self);
    template <typename Archive, typename Ring>
    void save(Archive& archive, std::shared_ptr<const exactreal::Module<Ring>> const& self);
    template <typename Archive, typename Ring>
    void load(Archive& archive, std::shared_ptr<const exactreal::Module<Ring>>& self);
}
```
