r"""
Finitely Generated Modules in the Real Numbers with Number Field Coefficients

The classes in this module wrap libexactreal for use in SageMath. They provide
:class:`ExactReals`, finitely generated submodules of the real modules over a
fixd real embedded number field.

EXAMPLES::

    sage: from pyexactreal import ExactReals
    sage: R = ExactReals(); R
    Real Numbers as (Rational Field)-Module

Typically, you want to fix some generators of your module. Here we take a
random number, modeling a transcendental real::

    sage: g = R.random_element(); g
    ℝ(0.120809…)

Mostly, you do not need to worry about the module structure of exact reals.
The module is automatically enlarged as needed::

    sage: g.module()
    ℚ-Module(ℝ(0.120809…))

    sage: (g * g).module()
    ℚ-Module(ℝ(0.120809…)^2)

    sage: (g + 1137).module()
    ℚ-Module(ℝ(0.120809…), 1)

"""
# ********************************************************************
#  This file is part of exact-real.
#
#        Copyright (C) 2019 Julian Rüth
#
#  exact-real is free software: you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation, either version 2 of the License, or
#  (at your option) any later version.
#
#  exact-real is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with exact-real. If not, see <https://www.gnu.org/licenses/>.
# ********************************************************************

from sage.all import QQ, UniqueRepresentation, ZZ, RR, Fields, Field, Morphism, Hom, SetsWithPartialMaps, NumberFieldElement, Parent, coerce
from sage.structure.element import FieldElement
from sage.categories.action import Action
from sage.structure.coerce import RightModuleAction
from pyexactreal import exactreal, QQModule, ZZModule, NumberFieldModule
from pyeantic import eantic, RealEmbeddedNumberField


class ExactRealElement(FieldElement):
    r"""
    An element of :class:`ExactReals`

    This is a simple wrapper of an ``exactreal::Element`` from libexactreal to
    make it work in the Parent/Element framework of SageMath.

    EXAMPLES::

        sage: from pyexactreal import ExactReals
        sage: r = ExactReals().random_element(); r
        ℝ(0.178808…)

    TESTS::

       sage: from pyexactreal.exact_reals import ExactRealElement
       sage: isinstance(r, ExactRealElement)
       True

    """
    def __init__(self, parent, value):
        if value == 0:
            value = parent._element_factory()
        if not isinstance(value, parent._element_factory):
            raise TypeError("element must be an %s" % (parent._element_factory,))
        self._backend = value
        FieldElement.__init__(self, parent)

    def module(self):
        r"""
        Return the ``exactreal::Module`` this element lives in.

        This is the actual underlying implementation from C++ and not a
        SageMath type. You usually should not have to use this.

        EXAMPLES::

            sage: from pyexactreal import ExactReals
            sage: ExactReals()(1).module()
            ℚ-Module(1)

        """
        return self._backend.module()

    def _add_(self, rhs):
        r"""
        Return the sum of this element and ``rhs``.

        EXAMPLES::

            sage: from pyexactreal import ExactReals
            sage: R = ExactReals()
            sage: R.random_element() + R.random_element()
            ℝ(0.478968…) + ℝ(0.782515…)
            sage: R.random_element() + 1337
            ℝ(0.621222…) + 1337

        """
        return self.parent()(self._backend + rhs._backend)

    def _sub_(self, rhs):
        r"""
        Return the difference of this element and ``rhs``.

        EXAMPLES::

            sage: from pyexactreal import ExactReals
            sage: R = ExactReals()
            sage: R.random_element() - R.random_element()
            ℝ(0.673083…) - ℝ(0.982253…)
            sage: R.random_element() - 1337
            ℝ(0.108391…) - 1337

        """
        return self.parent()(self._backend - rhs._backend)

    def _mul_(self, rhs):
        r"""
        Return the product of this element and ``rhs``.

        EXAMPLES::

            sage: from pyexactreal import ExactReals
            sage: R = ExactReals()
            sage: R.random_element() * R.random_element() # order of factors not deterministic
            ℝ(...)*ℝ(...)

        """
        return self.parent()(self._backend * rhs._backend)

    def _div_(self, rhs):
        r"""
        Return the quotient of this element and ``rhs``.

        This only works when the quotient is contained in the same module as
        the dividend.

        EXAMPLES::

            sage: from pyexactreal import ExactReals
            sage: R = ExactReals()
            sage: R.random_element() / R.random_element()
            Traceback (most recent call last):
            ...
            pyexactreal.cppyy_exactreal.NotRepresentableError: ...

            sage: x = R.random_element()
            sage: x / x
            1

            sage: R.random_element() / 1337
            1/1337*ℝ(...)

        """
        return self.base_ring()(self._backend / rhs._backend)

    def _neg_(self):
        r"""
        Return the negative of this element.

        EXAMPLES::

            sage: from pyexactreal import ExactReals
            sage: R = ExactReals()
            sage: -R.random_element()
            -ℝ(...)

        """
        return self.parent()(-self._backend)

    def _repr_(self):
        r"""
        Return a printable representation of this element.

        EXAMPLES::

            sage: from pyexactreal import ExactReals
            sage: R = ExactReals()
            sage: R.random_element()
            ℝ(...)

        """
        return repr(self._backend)

    def _cmp_(self, rhs):
        r"""
        EXAMPLES::

            sage: from pyexactreal import ExactReals
            sage: R = ExactReals()
            sage: x = R.random_element() # a random element in [0, 1]
            sage: x > -x
            True
            sage: x < -x
            False
            sage: -x < x
            True
            sage: -x > x
            False
            sage: -x == -x
            True
            sage: x == -x
            False

        """
        if self._backend < rhs._backend:
            return -1
        elif self._backend == rhs._backend:
            return 0
        else:
            return 1

    def _rmul_(self, c):
        r"""
        Return the product of this element with the constant ``c``::

            sage: from pyexactreal import ExactReals
            sage: R = ExactReals()
            sage: R.random_element() * 1337
            1337*ℝ(...)

        """
        return self._lmul_(c)

    def _lmul_(self, c):
        r"""
        Return the product of this element with the constant ``c``::

            sage: from pyexactreal import ExactReals
            sage: R = ExactReals()
            sage: 1337 * R.random_element()
            1337*ℝ(...)

        """
        base = self.parent().base()
        if base.has_coerce_map_from(c.parent()):
            c = coerce(base, c)
            if base is QQ:
                c = cppyy.gbl.mpq_class(str(c))
            else:
                c = c.renf_elem
            return self.parent()(c * self._backend)
        else:
            # assuming that this is a module element as well
            return self.parent()(c._backend * self._backend)

class ExactReals(UniqueRepresentation, Field):
    r"""
    The Real Numbers as a module over the number field ``base``.

    This serves as a common parent for all exact-real elements, i.e., elements
    in a finite module with transcendental or rational generators.

    EXAMPLES::

        sage: from pyexactreal import ExactReals
        sage: ExactReals()
        Real Numbers as (Rational Field)-Module
        sage: K.<a> = NumberField(x^2 - 2, embedding=AA(sqrt(2)))
        sage: ExactReals(K)
        Real Numbers as (Number Field in a with defining polynomial x^2 - 2 with a = 1.414213562373095?)-Module

    """
    @staticmethod
    def __classcall__(cls, base=None, category=None):
        r"""
        Normalize arguments so that this is a unique parent.

        TESTS::

            sage: from pyexactreal import ExactReals
            sage: ExactReals() is ExactReals(QQ)
            True

        """
        base = base or QQ
        category = category or Fields(base)
        return super(ExactReals, cls).__classcall__(cls, base, category)

    def __init__(self, base=None, category=None):
        if base is QQ:
            self._element_factory = exactreal.Element[type(exactreal.RationalField())]
            self._module_factory = lambda gens: QQModule(*gens)
        else:
            base = RealEmbeddedNumberField(base)
            ring = exactreal.NumberField(base.renf)
            self._element_factory = exactreal.Element[type(ring)]
            self._module_factory = lambda gens: NumberFieldModule(ring, *gens)

        Field.__init__(self, base, category=category or Fields())
        H = Hom(base, self)
        coercion = H.__make_element_class__(CoercionExactRealsNumberField)(H)
        self.register_coercion(coercion)

    def _repr_(self):
        r"""
        Return a printable represntation of this parent.

        EXAMPLES::

            sage: from pyexactreal import ExactReals
            sage: ExactReals(QQ)
            Real Numbers as (Rational Field)-Module

        """
        return "Real Numbers as (%s)-Module"%(self.base(),)

    def characteristic(self):
        r"""
        Return zero, the characteristic of the reals.

        EXAMPLES::

            sage: from pyexactreal import ExactReals
            sage: ExactReals().characteristic()
            0

        """
        return ZZ(0)

    def an_element(self):
        r"""
        Return a typical element of a finitely generated module.

        EXAMPLES::

            sage: from pyexactreal import ExactReals
            sage: ExactReals().an_element()
            0

        """
        return self(self._element_factory())

    def random_element(self):
        r"""
        Return a random real element.

        EXAMPLES::

            sage: from pyexactreal import ExactReals
            sage: ExactReals().random_element()
            ℝ(...)

        """
        module = self._module_factory([exactreal.RealNumber.random()])
        return self(self._element_factory(module, [1]))

    def rational(self, q):
        r"""
        Return the rational ``q`` as the element generating the module
        generated by ``q``. Note that this is not the same as ``q`` times the
        generator of the module generated by ``1``.

        EXAMPLES::

            sage: from pyexactreal import ExactReals
            sage: x = ExactReals().rational(2); x
            2
            sage: y = ExactReals().rational(3); y
            3
            sage: x + y
            Traceback (most recent call last):
            ...
            Exception: ... at most one generator can be rational ...

        """
        module = self._module_factory([exactreal.RealNumber.rational(q)])
        return self(self._element_factory(module, [1]))

    Element = ExactRealElement


class CoercionExactRealsNumberField(Morphism):
    r"""
    Coercion morphism from a number field to the exact reals over that number
    field.

    EXAMPLES::

        sage: from pyexactreal import ExactReals
        sage: R = ExactReals(QQ)
        sage: R.coerce_map_from(QQ)
        Generic morphism:
          From: Rational Field
          To:   Real Numbers as (Rational Field)-Module

    """
    def _call_(self, x):
        return x * self.codomain().rational(1)


# This should eventually go into its own library:
# https://github.com/flatsurf/exact-real/issues/66
import cppyy
class ConversionZZMpz(Morphism):
    def __init__(self):
        Morphism.__init__(self, Hom(cppyy.gbl.mpz_class, ZZ, ZZ.category(), check=False))

    def _call_(self, x):
        # this could certainly be done faster in Cython with the underlying mpz_t
        return ZZ(x.get_str())


class ConversionQQMpq(Morphism):
    def __init__(self):
        Morphism.__init__(self, Hom(cppyy.gbl.mpq_class, QQ, QQ.category(), check=False))
    
    def _call_(self, x):
        # this could certainly be done faster in Cython with the underlying mpq_t
        return QQ(x.get_str())

cppyy.gbl.mpz_class.is_exact = lambda: True
ZZ.register_conversion(ConversionZZMpz())

cppyy.gbl.mpq_class.is_exact = lambda: True
QQ.register_conversion(ConversionQQMpq())