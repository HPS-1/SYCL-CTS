"""Represents an argument or return type. The type may be generic."""
class argtype:
    def __init__(self, name, var_type, base_type, dim, child_types):
        self.name = name # Type name. This works also as an identifier for the type.
        self.var_type = var_type # Variable type (scalar,vector or NULL). Generic types should have a NULL variable type.
        self.base_type = base_type # The base type (e.g. the base type of sycl::double3 is double). Generic types should have a NULL base type.
        self.dim = dim # Dimensionality of the type. Generic types should have this as zero.
        self.child_types = child_types # Contains the list of types which this type can be decomposed to. Basic types should accept an empty list.
    def __eq__(self, other):
        if isinstance(other, argtype):
            return (self.name == other.name)
    def __ne__(self, other):
        return (not self.__eq__(other))
    def __hash__(self):
        return hash(self.name)

def create_basic_types():
    type_dic = {}

    # Basic Types

    t_bool_0 = argtype("bool", "scalar", "bool", 1, [])
    type_dic["bool"] = t_bool_0


    t_float_0 = argtype("float", "scalar", "float", 1, [])
    type_dic["float"] = t_float_0

    t_vfloat_2 = argtype("sycl::vec<float, 2>", "vector", "float", 2, [])
    type_dic["sycl::vec<float, 2>"] = t_vfloat_2

    t_vfloat_3 = argtype("sycl::vec<float, 3>", "vector", "float", 3, [])
    type_dic["sycl::vec<float, 3>"] = t_vfloat_3

    t_vfloat_4 = argtype("sycl::vec<float, 4>", "vector", "float", 4, [])
    type_dic["sycl::vec<float, 4>"] = t_vfloat_4

    t_vfloat_8 = argtype("sycl::vec<float, 8>", "vector", "float", 8, [])
    type_dic["sycl::vec<float, 8>"] = t_vfloat_8

    t_vfloat_16 = argtype("sycl::vec<float, 16>", "vector", "float", 16, [])
    type_dic["sycl::vec<float, 16>"] = t_vfloat_16

    t_mfloat_2 = argtype("sycl::marray<float, 2>", "marray", "float", 2, [])
    type_dic["sycl::marray<float, 2>"] = t_mfloat_2

    t_mfloat_3 = argtype("sycl::marray<float, 3>", "marray", "float", 3, [])
    type_dic["sycl::marray<float, 3>"] = t_mfloat_3

    t_mfloat_4 = argtype("sycl::marray<float, 4>", "marray", "float", 4, [])
    type_dic["sycl::marray<float, 4>"] = t_mfloat_4

    t_mfloat_5 = argtype("sycl::marray<float, 5>", "marray", "float", 5, [])
    type_dic["sycl::marray<float, 5>"] = t_mfloat_5

    t_mfloat_17 = argtype("sycl::marray<float, 17>", "marray", "float", 17, [])
    type_dic["sycl::marray<float, 17>"] = t_mfloat_17


    t_double_0 = argtype("double", "scalar", "double", 1, [])
    type_dic["double"] = t_double_0

    t_vdouble_2 = argtype("sycl::vec<double, 2>", "vector", "double", 2, [])
    type_dic["sycl::vec<double, 2>"] = t_vdouble_2

    t_vdouble_3 = argtype("sycl::vec<double, 3>", "vector", "double", 3, [])
    type_dic["sycl::vec<double, 3>"] = t_vdouble_3

    t_vdouble_4 = argtype("sycl::vec<double, 4>", "vector", "double", 4, [])
    type_dic["sycl::vec<double, 4>"] = t_vdouble_4

    t_vdouble_8 = argtype("sycl::vec<double, 8>", "vector", "double", 8, [])
    type_dic["sycl::vec<double, 8>"] = t_vdouble_8

    t_vdouble_16 = argtype("sycl::vec<double, 16>", "vector", "double", 16, [])
    type_dic["sycl::vec<double, 16>"] = t_vdouble_16

    t_mdouble_2 = argtype("sycl::marray<double, 2>", "marray", "double", 2, [])
    type_dic["sycl::marray<double, 2>"] = t_mdouble_2

    t_mdouble_3 = argtype("sycl::marray<double, 3>", "marray", "double", 3, [])
    type_dic["sycl::marray<double, 3>"] = t_mdouble_3

    t_mdouble_4 = argtype("sycl::marray<double, 4>", "marray", "double", 4, [])
    type_dic["sycl::marray<double, 4>"] = t_mdouble_4

    t_mdouble_5 = argtype("sycl::marray<double, 5>", "marray", "double", 5, [])
    type_dic["sycl::marray<double, 5>"] = t_mdouble_5

    t_mdouble_17 = argtype("sycl::marray<double, 17>", "marray", "double", 17, [])
    type_dic["sycl::marray<double, 17>"] = t_mdouble_17


    t_half_0 = argtype("sycl::half", "scalar", "sycl::half", 1, [])
    type_dic["sycl::half"] = t_half_0

    t_vhalf_2 = argtype("sycl::vec<sycl::half, 2>", "vector", "sycl::half", 2, [])
    type_dic["sycl::vec<sycl::half, 2>"] = t_vhalf_2

    t_vhalf_3 = argtype("sycl::vec<sycl::half, 3>", "vector", "sycl::half", 3, [])
    type_dic["sycl::vec<sycl::half, 3>"] = t_vhalf_3

    t_vhalf_4 = argtype("sycl::vec<sycl::half, 4>", "vector", "sycl::half", 4, [])
    type_dic["sycl::vec<sycl::half, 4>"] = t_vhalf_4

    t_vhalf_8 = argtype("sycl::vec<sycl::half, 8>", "vector", "sycl::half", 8, [])
    type_dic["sycl::vec<sycl::half, 8>"] = t_vhalf_8

    t_vhalf_16 = argtype("sycl::vec<sycl::half, 16>", "vector", "sycl::half", 16, [])
    type_dic["sycl::vec<sycl::half, 16>"] = t_vhalf_16

    t_mhalf_2 = argtype("sycl::marray<sycl::half, 2>", "marray", "sycl::half", 2, [])
    type_dic["sycl::marray<sycl::half, 2>"] = t_mhalf_2

    t_mhalf_3 = argtype("sycl::marray<sycl::half, 3>", "marray", "sycl::half", 3, [])
    type_dic["sycl::marray<sycl::half, 3>"] = t_mhalf_3

    t_mhalf_4 = argtype("sycl::marray<sycl::half, 4>", "marray", "sycl::half", 4, [])
    type_dic["sycl::marray<sycl::half, 4>"] = t_mhalf_4

    t_mhalf_5 = argtype("sycl::marray<sycl::half, 5>", "marray", "sycl::half", 5, [])
    type_dic["sycl::marray<sycl::half, 5>"] = t_mhalf_5

    t_mhalf_17 = argtype("sycl::marray<sycl::half, 17>", "marray", "sycl::half", 17, [])
    type_dic["sycl::marray<sycl::half, 17>"] = t_mhalf_17


    t_char_0 = argtype("char", "scalar", "char", 1, [])
    type_dic["char"] = t_char_0

    t_vchar_2 = argtype("sycl::vec<char, 2>", "vector", "char", 2, [])
    type_dic["sycl::vec<char, 2>"] = t_vchar_2

    t_vchar_3 = argtype("sycl::vec<char, 3>", "vector", "char", 3, [])
    type_dic["sycl::vec<char, 3>"] = t_vchar_3

    t_vchar_4 = argtype("sycl::vec<char, 4>", "vector", "char", 4, [])
    type_dic["sycl::vec<char, 4>"] = t_vchar_4

    t_vchar_8 = argtype("sycl::vec<char, 8>", "vector", "char", 8, [])
    type_dic["sycl::vec<char, 8>"] = t_vchar_8

    t_vchar_16 = argtype("sycl::vec<char, 16>", "vector", "char", 16, [])
    type_dic["sycl::vec<char, 16>"] = t_vchar_16

    t_mchar_2 = argtype("sycl::marray<char, 2>", "marray", "char", 2, [])
    type_dic["sycl::marray<char, 2>"] = t_mchar_2

    t_mchar_3 = argtype("sycl::marray<char, 3>", "marray", "char", 3, [])
    type_dic["sycl::marray<char, 3>"] = t_mchar_3

    t_mchar_4 = argtype("sycl::marray<char, 4>", "marray", "char", 4, [])
    type_dic["sycl::marray<char, 4>"] = t_mchar_4

    t_mchar_5 = argtype("sycl::marray<char, 5>", "marray", "char", 5, [])
    type_dic["sycl::marray<char, 5>"] = t_mchar_5

    t_mchar_17 = argtype("sycl::marray<char, 17>", "marray", "char", 17, [])
    type_dic["sycl::marray<char, 17>"] = t_mchar_17


    t_schar_0 = argtype("signed char", "scalar", "signed char", 1, [])
    type_dic["signed char"] = t_schar_0

    t_vschar_2 = argtype("sycl::vec<signed char, 2>", "vector", "signed char", 2, [])
    type_dic["sycl::vec<signed char, 2>"] = t_vschar_2

    t_vschar_3 = argtype("sycl::vec<signed char, 3>", "vector", "signed char", 3, [])
    type_dic["sycl::vec<signed char, 3>"] = t_vschar_3

    t_vschar_4 = argtype("sycl::vec<signed char, 4>", "vector", "signed char", 4, [])
    type_dic["sycl::vec<signed char, 4>"] = t_vschar_4

    t_vschar_8 = argtype("sycl::vec<signed char, 8>", "vector", "signed char", 8, [])
    type_dic["sycl::vec<signed char, 8>"] = t_vschar_8

    t_vschar_16 = argtype("sycl::vec<signed char, 16>", "vector", "signed char", 16, [])
    type_dic["sycl::vec<signed char, 16>"] = t_vschar_16

    t_mschar_2 = argtype("sycl::marray<signed char, 2>", "marray", "signed char", 2, [])
    type_dic["sycl::marray<signed char, 2>"] = t_mschar_2

    t_mschar_3 = argtype("sycl::marray<signed char, 3>", "marray", "signed char", 3, [])
    type_dic["sycl::marray<signed char, 3>"] = t_mschar_3

    t_mschar_4 = argtype("sycl::marray<signed char, 4>", "marray", "signed char", 4, [])
    type_dic["sycl::marray<signed char, 4>"] = t_mschar_4

    t_mschar_5 = argtype("sycl::marray<signed char, 5>", "marray", "signed char", 5, [])
    type_dic["sycl::marray<signed char, 5>"] = t_mschar_5

    t_mschar_17 = argtype("sycl::marray<signed char, 17>", "marray", "signed char", 17, [])
    type_dic["sycl::marray<signed char, 17>"] = t_mschar_17


    t_uchar_0 = argtype("unsigned char", "scalar", "unsigned char", 1, [])
    type_dic["unsigned char"] = t_uchar_0

    t_vuchar_2 = argtype("sycl::vec<unsigned char, 2>", "vector", "unsigned char", 2, [])
    type_dic["sycl::vec<unsigned char, 2>"] = t_vuchar_2

    t_vuchar_3 = argtype("sycl::vec<unsigned char, 3>", "vector", "unsigned char", 3, [])
    type_dic["sycl::vec<unsigned char, 3>"] = t_vuchar_3

    t_vuchar_4 = argtype("sycl::vec<unsigned char, 4>", "vector", "unsigned char", 4, [])
    type_dic["sycl::vec<unsigned char, 4>"] = t_vuchar_4

    t_vuchar_8 = argtype("sycl::vec<unsigned char, 8>", "vector", "unsigned char", 8, [])
    type_dic["sycl::vec<unsigned char, 8>"] = t_vuchar_8

    t_vuchar_16 = argtype("sycl::vec<unsigned char, 16>", "vector", "unsigned char", 16, [])
    type_dic["sycl::vec<unsigned char, 16>"] = t_vuchar_16

    t_muchar_2 = argtype("sycl::marray<unsigned char, 2>", "marray", "unsigned char", 2, [])
    type_dic["sycl::marray<unsigned char, 2>"] = t_muchar_2

    t_muchar_3 = argtype("sycl::marray<unsigned char, 3>", "marray", "unsigned char", 3, [])
    type_dic["sycl::marray<unsigned char, 3>"] = t_muchar_3

    t_muchar_4 = argtype("sycl::marray<unsigned char, 4>", "marray", "unsigned char", 4, [])
    type_dic["sycl::marray<unsigned char, 4>"] = t_muchar_4

    t_muchar_5 = argtype("sycl::marray<unsigned char, 5>", "marray", "unsigned char", 5, [])
    type_dic["sycl::marray<unsigned char, 5>"] = t_muchar_5

    t_muchar_17 = argtype("sycl::marray<unsigned char, 17>", "marray", "unsigned char", 17, [])
    type_dic["sycl::marray<unsigned char, 17>"] = t_muchar_17


    t_short_0 = argtype("short", "scalar", "short", 1, [])
    type_dic["short"] = t_short_0

    t_vshort_2 = argtype("sycl::vec<short, 2>", "vector", "short", 2, [])
    type_dic["sycl::vec<short, 2>"] = t_vshort_2

    t_vshort_3 = argtype("sycl::vec<short, 3>", "vector", "short", 3, [])
    type_dic["sycl::vec<short, 3>"] = t_vshort_3

    t_vshort_4 = argtype("sycl::vec<short, 4>", "vector", "short", 4, [])
    type_dic["sycl::vec<short, 4>"] = t_vshort_4

    t_vshort_8 = argtype("sycl::vec<short, 8>", "vector", "short", 8, [])
    type_dic["sycl::vec<short, 8>"] = t_vshort_8

    t_vshort_16 = argtype("sycl::vec<short, 16>", "vector", "short", 16, [])
    type_dic["sycl::vec<short, 16>"] = t_vshort_16

    t_mshort_2 = argtype("sycl::marray<short, 2>", "marray", "short", 2, [])
    type_dic["sycl::marray<short, 2>"] = t_mshort_2

    t_mshort_3 = argtype("sycl::marray<short, 3>", "marray", "short", 3, [])
    type_dic["sycl::marray<short, 3>"] = t_mshort_3

    t_mshort_4 = argtype("sycl::marray<short, 4>", "marray", "short", 4, [])
    type_dic["sycl::marray<short, 4>"] = t_mshort_4

    t_mshort_5 = argtype("sycl::marray<short, 5>", "marray", "short", 5, [])
    type_dic["sycl::marray<short, 5>"] = t_mshort_5

    t_mshort_17 = argtype("sycl::marray<short, 17>", "marray", "short", 17, [])
    type_dic["sycl::marray<short, 17>"] = t_mshort_17


    t_ushort_0 = argtype("unsigned short", "scalar", "unsigned short", 1, [])
    type_dic["unsigned short"] = t_ushort_0

    t_vushort_2 = argtype("sycl::vec<unsigned short, 2>", "vector", "unsigned short", 2, [])
    type_dic["sycl::vec<unsigned short, 2>"] = t_vushort_2

    t_vushort_3 = argtype("sycl::vec<unsigned short, 3>", "vector", "unsigned short", 3, [])
    type_dic["sycl::vec<unsigned short, 3>"] = t_vushort_3

    t_vushort_4 = argtype("sycl::vec<unsigned short, 4>", "vector", "unsigned short", 4, [])
    type_dic["sycl::vec<unsigned short, 4>"] = t_vushort_4

    t_vushort_8 = argtype("sycl::vec<unsigned short, 8>", "vector", "unsigned short", 8, [])
    type_dic["sycl::vec<unsigned short, 8>"] = t_vushort_8

    t_vushort_16 = argtype("sycl::vec<unsigned short, 16>", "vector", "unsigned short", 16, [])
    type_dic["sycl::vec<unsigned short, 16>"] = t_vushort_16

    t_mushort_2 = argtype("sycl::marray<unsigned short, 2>", "marray", "unsigned short", 2, [])
    type_dic["sycl::marray<unsigned short, 2>"] = t_mushort_2

    t_mushort_3 = argtype("sycl::marray<unsigned short, 3>", "marray", "unsigned short", 3, [])
    type_dic["sycl::marray<unsigned short, 3>"] = t_mushort_3

    t_mushort_4 = argtype("sycl::marray<unsigned short, 4>", "marray", "unsigned short", 4, [])
    type_dic["sycl::marray<unsigned short, 4>"] = t_mushort_4

    t_mushort_5 = argtype("sycl::marray<unsigned short, 5>", "marray", "unsigned short", 5, [])
    type_dic["sycl::marray<unsigned short, 5>"] = t_mushort_5

    t_mushort_17 = argtype("sycl::marray<unsigned short, 17>", "marray", "unsigned short", 17, [])
    type_dic["sycl::marray<unsigned short, 17>"] = t_mushort_17


    t_int_0 = argtype("int", "scalar", "int", 1, [])
    type_dic["int"] = t_int_0

    t_vint_2 = argtype("sycl::vec<int, 2>", "vector", "int", 2, [])
    type_dic["sycl::vec<int, 2>"] = t_vint_2

    t_vint_3 = argtype("sycl::vec<int, 3>", "vector", "int", 3, [])
    type_dic["sycl::vec<int, 3>"] = t_vint_3

    t_vint_4 = argtype("sycl::vec<int, 4>", "vector", "int", 4, [])
    type_dic["sycl::vec<int, 4>"] = t_vint_4

    t_vint_8 = argtype("sycl::vec<int, 8>", "vector", "int", 8, [])
    type_dic["sycl::vec<int, 8>"] = t_vint_8

    t_vint_16 = argtype("sycl::vec<int, 16>", "vector", "int", 16, [])
    type_dic["sycl::vec<int, 16>"] = t_vint_16

    t_mint_2 = argtype("sycl::marray<int, 2>", "marray", "int", 2, [])
    type_dic["sycl::marray<int, 2>"] = t_mint_2

    t_mint_3 = argtype("sycl::marray<int, 3>", "marray", "int", 3, [])
    type_dic["sycl::marray<int, 3>"] = t_mint_3

    t_mint_4 = argtype("sycl::marray<int, 4>", "marray", "int", 4, [])
    type_dic["sycl::marray<int, 4>"] = t_mint_4

    t_mint_5 = argtype("sycl::marray<int, 5>", "marray", "int", 5, [])
    type_dic["sycl::marray<int, 5>"] = t_mint_5

    t_mint_17 = argtype("sycl::marray<int, 17>", "marray", "int", 17, [])
    type_dic["sycl::marray<int, 17>"] = t_mint_17


    t_uint_0 = argtype("unsigned", "scalar", "unsigned", 1, [])
    type_dic["unsigned"] = t_uint_0

    t_vuint_2 = argtype("sycl::vec<unsigned, 2>", "vector", "unsigned", 2, [])
    type_dic["sycl::vec<unsigned, 2>"] = t_vuint_2

    t_vuint_3 = argtype("sycl::vec<unsigned, 3>", "vector", "unsigned", 3, [])
    type_dic["sycl::vec<unsigned, 3>"] = t_vuint_3

    t_vuint_4 = argtype("sycl::vec<unsigned, 4>", "vector", "unsigned", 4, [])
    type_dic["sycl::vec<unsigned, 4>"] = t_vuint_4

    t_vuint_8 = argtype("sycl::vec<unsigned, 8>", "vector", "unsigned", 8, [])
    type_dic["sycl::vec<unsigned, 8>"] = t_vuint_8

    t_vuint_16 = argtype("sycl::vec<unsigned, 16>", "vector", "unsigned", 16, [])
    type_dic["sycl::vec<unsigned, 16>"] = t_vuint_16

    t_muint_2 = argtype("sycl::marray<unsigned, 2>", "marray", "unsigned", 2, [])
    type_dic["sycl::marray<unsigned, 2>"] = t_muint_2

    t_muint_3 = argtype("sycl::marray<unsigned, 3>", "marray", "unsigned", 3, [])
    type_dic["sycl::marray<unsigned, 3>"] = t_muint_3

    t_muint_4 = argtype("sycl::marray<unsigned, 4>", "marray", "unsigned", 4, [])
    type_dic["sycl::marray<unsigned, 4>"] = t_muint_4

    t_muint_5 = argtype("sycl::marray<unsigned, 5>", "marray", "unsigned", 5, [])
    type_dic["sycl::marray<unsigned, 5>"] = t_muint_5

    t_muint_17 = argtype("sycl::marray<unsigned, 17>", "marray", "unsigned", 17, [])
    type_dic["sycl::marray<unsigned, 17>"] = t_muint_17


    t_long_0 = argtype("long", "scalar", "long", 1, [])
    type_dic["long"] = t_long_0

    t_vlong_2 = argtype("sycl::vec<long, 2>", "vector", "long", 2, [])
    type_dic["sycl::vec<long, 2>"] = t_vlong_2

    t_vlong_3 = argtype("sycl::vec<long, 3>", "vector", "long", 3, [])
    type_dic["sycl::vec<long, 3>"] = t_vlong_3

    t_vlong_4 = argtype("sycl::vec<long, 4>", "vector", "long", 4, [])
    type_dic["sycl::vec<long, 4>"] = t_vlong_4

    t_vlong_8 = argtype("sycl::vec<long, 8>", "vector", "long", 8, [])
    type_dic["sycl::vec<long, 8>"] = t_vlong_8

    t_vlong_16 = argtype("sycl::vec<long, 16>", "vector", "long", 16, [])
    type_dic["sycl::vec<long, 16>"] = t_vlong_16

    t_mlong_2 = argtype("sycl::marray<long, 2>", "marray", "long", 2, [])
    type_dic["sycl::marray<long, 2>"] = t_mlong_2

    t_mlong_3 = argtype("sycl::marray<long, 3>", "marray", "long", 3, [])
    type_dic["sycl::marray<long, 3>"] = t_mlong_3

    t_mlong_4 = argtype("sycl::marray<long, 4>", "marray", "long", 4, [])
    type_dic["sycl::marray<long, 4>"] = t_mlong_4

    t_mlong_5 = argtype("sycl::marray<long, 5>", "marray", "long", 5, [])
    type_dic["sycl::marray<long, 5>"] = t_mlong_5

    t_mlong_17 = argtype("sycl::marray<long, 17>", "marray", "long", 17, [])
    type_dic["sycl::marray<long, 17>"] = t_mlong_17


    t_ulong_0 = argtype("unsigned long", "scalar", "unsigned long", 1, [])
    type_dic["unsigned long"] = t_ulong_0

    t_vulong_2 = argtype("sycl::vec<unsigned long, 2>", "vector", "unsigned long", 2, [])
    type_dic["sycl::vec<unsigned long, 2>"] = t_vulong_2

    t_vulong_3 = argtype("sycl::vec<unsigned long, 3>", "vector", "unsigned long", 3, [])
    type_dic["sycl::vec<unsigned long, 3>"] = t_vulong_3

    t_vulong_4 = argtype("sycl::vec<unsigned long, 4>", "vector", "unsigned long", 4, [])
    type_dic["sycl::vec<unsigned long, 4>"] = t_vulong_4

    t_vulong_8 = argtype("sycl::vec<unsigned long, 8>", "vector", "unsigned long", 8, [])
    type_dic["sycl::vec<unsigned long, 8>"] = t_vulong_8

    t_vulong_16 = argtype("sycl::vec<unsigned long, 16>", "vector", "unsigned long", 16, [])
    type_dic["sycl::vec<unsigned long, 16>"] = t_vulong_16

    t_mulong_2 = argtype("sycl::marray<unsigned long, 2>", "marray", "unsigned long", 2, [])
    type_dic["sycl::marray<unsigned long, 2>"] = t_mulong_2

    t_mulong_3 = argtype("sycl::marray<unsigned long, 3>", "marray", "unsigned long", 3, [])
    type_dic["sycl::marray<unsigned long, 3>"] = t_mulong_3

    t_mulong_4 = argtype("sycl::marray<unsigned long, 4>", "marray", "unsigned long", 4, [])
    type_dic["sycl::marray<unsigned long, 4>"] = t_mulong_4

    t_mulong_5 = argtype("sycl::marray<unsigned long, 5>", "marray", "unsigned long", 5, [])
    type_dic["sycl::marray<unsigned long, 5>"] = t_mulong_5

    t_mulong_17 = argtype("sycl::marray<unsigned long, 17>", "marray", "unsigned long", 17, [])
    type_dic["sycl::marray<unsigned long, 17>"] = t_mulong_17


    t_longlong_0 = argtype("long long", "scalar", "long long", 1, [])
    type_dic["long long"] = t_longlong_0

    t_vlonglong_2 = argtype("sycl::vec<long long, 2>", "vector", "long long", 2, [])
    type_dic["sycl::vec<long long, 2>"] = t_vlonglong_2

    t_vlonglong_3 = argtype("sycl::vec<long long, 3>", "vector", "long long", 3, [])
    type_dic["sycl::vec<long long, 3>"] = t_vlonglong_3

    t_vlonglong_4 = argtype("sycl::vec<long long, 4>", "vector", "long long", 4, [])
    type_dic["sycl::vec<long long, 4>"] = t_vlonglong_4

    t_vlonglong_8 = argtype("sycl::vec<long long, 8>", "vector", "long long", 8, [])
    type_dic["sycl::vec<long long, 8>"] = t_vlonglong_8

    t_vlonglong_16 = argtype("sycl::vec<long long, 16>", "vector", "long long", 16, [])
    type_dic["sycl::vec<long long, 16>"] = t_vlonglong_16

    t_mlonglong_2 = argtype("sycl::marray<long long, 2>", "marray", "long long", 2, [])
    type_dic["sycl::marray<long long, 2>"] = t_mlonglong_2

    t_mlonglong_3 = argtype("sycl::marray<long long, 3>", "marray", "long long", 3, [])
    type_dic["sycl::marray<long long, 3>"] = t_mlonglong_3

    t_mlonglong_4 = argtype("sycl::marray<long long, 4>", "marray", "long long", 4, [])
    type_dic["sycl::marray<long long, 4>"] = t_mlonglong_4

    t_mlonglong_5 = argtype("sycl::marray<long long, 5>", "marray", "long long", 5, [])
    type_dic["sycl::marray<long long, 5>"] = t_mlonglong_5

    t_mlonglong_17 = argtype("sycl::marray<long long, 17>", "marray", "long long", 17, [])
    type_dic["sycl::marray<long long, 17>"] = t_mlonglong_17


    t_ulonglong_0 = argtype("unsigned long long", "scalar", "unsigned long long", 1, [])
    type_dic["unsigned long long"] = t_ulonglong_0

    t_vulonglong_2 = argtype("sycl::vec<unsigned long long, 2>", "vector", "unsigned long long", 2, [])
    type_dic["sycl::vec<unsigned long long, 2>"] = t_vulonglong_2

    t_vulonglong_3 = argtype("sycl::vec<unsigned long long, 3>", "vector", "unsigned long long", 3, [])
    type_dic["sycl::vec<unsigned long long, 3>"] = t_vulonglong_3

    t_vulonglong_4 = argtype("sycl::vec<unsigned long long, 4>", "vector", "unsigned long long", 4, [])
    type_dic["sycl::vec<unsigned long long, 4>"] = t_vulonglong_4

    t_vulonglong_8 = argtype("sycl::vec<unsigned long long, 8>", "vector", "unsigned long long", 8, [])
    type_dic["sycl::vec<unsigned long long, 8>"] = t_vulonglong_8

    t_vulonglong_16 = argtype("sycl::vec<unsigned long long, 16>", "vector", "unsigned long long", 16, [])
    type_dic["sycl::vec<unsigned long long, 16>"] = t_vulonglong_16

    t_mulonglong_2 = argtype("sycl::marray<unsigned long long, 2>", "marray", "unsigned long long", 2, [])
    type_dic["sycl::marray<unsigned long long, 2>"] = t_mulonglong_2

    t_mulonglong_3 = argtype("sycl::marray<unsigned long long, 3>", "marray", "unsigned long long", 3, [])
    type_dic["sycl::marray<unsigned long long, 3>"] = t_mulonglong_3

    t_mulonglong_4 = argtype("sycl::marray<unsigned long long, 4>", "marray", "unsigned long long", 4, [])
    type_dic["sycl::marray<unsigned long long, 4>"] = t_mulonglong_4

    t_mulonglong_5 = argtype("sycl::marray<unsigned long long, 5>", "marray", "unsigned long long", 5, [])
    type_dic["sycl::marray<unsigned long long, 5>"] = t_mulonglong_5

    t_mulonglong_17 = argtype("sycl::marray<unsigned long long, 17>", "marray", "unsigned long long", 17, [])
    type_dic["sycl::marray<unsigned long long, 17>"] = t_mulonglong_17


    # Fixed size basic types

    t_int8t_0 = argtype("int8_t", "scalar", "int8_t", 1, [])
    type_dic["int8_t"] = t_int8t_0

    t_vint8t_2 = argtype("sycl::vec<int8_t, 2>", "vector", "int8_t", 2, [])
    type_dic["sycl::vec<int8_t, 2>"] = t_vint8t_2

    t_vint8t_3 = argtype("sycl::vec<int8_t, 3>", "vector", "int8_t", 3, [])
    type_dic["sycl::vec<int8_t, 3>"] = t_vint8t_3

    t_vint8t_4 = argtype("sycl::vec<int8_t, 4>", "vector", "int8_t", 4, [])
    type_dic["sycl::vec<int8_t, 4>"] = t_vint8t_4

    t_vint8t_8 = argtype("sycl::vec<int8_t, 8>", "vector", "int8_t", 8, [])
    type_dic["sycl::vec<int8_t, 8>"] = t_vint8t_8

    t_vint8t_16 = argtype("sycl::vec<int8_t, 16>", "vector", "int8_t", 16, [])
    type_dic["sycl::vec<int8_t, 16>"] = t_vint8t_16

    t_mint8t_2 = argtype("sycl::marray<int8_t, 2>", "marray", "int8_t", 2, [])
    type_dic["sycl::marray<int8_t, 2>"] = t_mint8t_2

    t_mint8t_3 = argtype("sycl::marray<int8_t, 3>", "marray", "int8_t", 3, [])
    type_dic["sycl::marray<int8_t, 3>"] = t_mint8t_3

    t_mint8t_4 = argtype("sycl::marray<int8_t, 4>", "marray", "int8_t", 4, [])
    type_dic["sycl::marray<int8_t, 4>"] = t_mint8t_4

    t_mint8t_5 = argtype("sycl::marray<int8_t, 5>", "marray", "int8_t", 5, [])
    type_dic["sycl::marray<int8_t, 5>"] = t_mint8t_5

    t_mint8t_17 = argtype("sycl::marray<int8_t, 17>", "marray", "int8_t", 17, [])
    type_dic["sycl::marray<int8_t, 17>"] = t_mint8t_17


    t_uint8t_0 = argtype("uint8_t", "scalar", "uint8_t", 1, [])
    type_dic["uint8_t"] = t_uint8t_0

    t_vuint8t_2 = argtype("sycl::vec<uint8_t, 2>", "vector", "uint8_t", 2, [])
    type_dic["sycl::vec<uint8_t, 2>"] = t_vuint8t_2

    t_vuint8t_3 = argtype("sycl::vec<uint8_t, 3>", "vector", "uint8_t", 3, [])
    type_dic["sycl::vec<uint8_t, 3>"] = t_vuint8t_3

    t_vuint8t_4 = argtype("sycl::vec<uint8_t, 4>", "vector", "uint8_t", 4, [])
    type_dic["sycl::vec<uint8_t, 4>"] = t_vuint8t_4

    t_vuint8t_8 = argtype("sycl::vec<uint8_t, 8>", "vector", "uint8_t", 8, [])
    type_dic["sycl::vec<uint8_t, 8>"] = t_vuint8t_8

    t_vuint8t_16 = argtype("sycl::vec<uint8_t, 16>", "vector", "uint8_t", 16, [])
    type_dic["sycl::vec<uint8_t, 16>"] = t_vuint8t_16

    t_muint8t_2 = argtype("sycl::marray<uint8_t, 2>", "marray", "uint8_t", 2, [])
    type_dic["sycl::marray<uint8_t, 2>"] = t_muint8t_2

    t_muint8t_3 = argtype("sycl::marray<uint8_t, 3>", "marray", "uint8_t", 3, [])
    type_dic["sycl::marray<uint8_t, 3>"] = t_muint8t_3

    t_muint8t_4 = argtype("sycl::marray<uint8_t, 4>", "marray", "uint8_t", 4, [])
    type_dic["sycl::marray<uint8_t, 4>"] = t_muint8t_4

    t_muint8t_5 = argtype("sycl::marray<uint8_t, 5>", "marray", "uint8_t", 5, [])
    type_dic["sycl::marray<uint8_t, 5>"] = t_muint8t_5

    t_muint8t_17 = argtype("sycl::marray<uint8_t, 17>", "marray", "uint8_t", 17, [])
    type_dic["sycl::marray<uint8_t, 17>"] = t_muint8t_17


    t_int16t_0 = argtype("int16_t", "scalar", "int16_t", 1, [])
    type_dic["int16_t"] = t_int16t_0

    t_vint16t_2 = argtype("sycl::vec<int16_t, 2>", "vector", "int16_t", 2, [])
    type_dic["sycl::vec<int16_t, 2>"] = t_vint16t_2

    t_vint16t_3 = argtype("sycl::vec<int16_t, 3>", "vector", "int16_t", 3, [])
    type_dic["sycl::vec<int16_t, 3>"] = t_vint16t_3

    t_vint16t_4 = argtype("sycl::vec<int16_t, 4>", "vector", "int16_t", 4, [])
    type_dic["sycl::vec<int16_t, 4>"] = t_vint16t_4

    t_vint16t_8 = argtype("sycl::vec<int16_t, 8>", "vector", "int16_t", 8, [])
    type_dic["sycl::vec<int16_t, 8>"] = t_vint16t_8

    t_vint16t_16 = argtype("sycl::vec<int16_t, 16>", "vector", "int16_t", 16, [])
    type_dic["sycl::vec<int16_t, 16>"] = t_vint16t_16

    t_mint16t_2 = argtype("sycl::marray<int16_t, 2>", "marray", "int16_t", 2, [])
    type_dic["sycl::marray<int16_t, 2>"] = t_mint16t_2

    t_mint16t_3 = argtype("sycl::marray<int16_t, 3>", "marray", "int16_t", 3, [])
    type_dic["sycl::marray<int16_t, 3>"] = t_mint16t_3

    t_mint16t_4 = argtype("sycl::marray<int16_t, 4>", "marray", "int16_t", 4, [])
    type_dic["sycl::marray<int16_t, 4>"] = t_mint16t_4

    t_mint16t_5 = argtype("sycl::marray<int16_t, 5>", "marray", "int16_t", 5, [])
    type_dic["sycl::marray<int16_t, 5>"] = t_mint16t_5

    t_mint16t_17 = argtype("sycl::marray<int16_t, 17>", "marray", "int16_t", 17, [])
    type_dic["sycl::marray<int16_t, 17>"] = t_mint16t_17


    t_uint16t_0 = argtype("uint16_t", "scalar", "uint16_t", 1, [])
    type_dic["uint16_t"] = t_uint16t_0

    t_vuint16t_2 = argtype("sycl::vec<uint16_t, 2>", "vector", "uint16_t", 2, [])
    type_dic["sycl::vec<uint16_t, 2>"] = t_vuint16t_2

    t_vuint16t_3 = argtype("sycl::vec<uint16_t, 3>", "vector", "uint16_t", 3, [])
    type_dic["sycl::vec<uint16_t, 3>"] = t_vuint16t_3

    t_vuint16t_4 = argtype("sycl::vec<uint16_t, 4>", "vector", "uint16_t", 4, [])
    type_dic["sycl::vec<uint16_t, 4>"] = t_vuint16t_4

    t_vuint16t_8 = argtype("sycl::vec<uint16_t, 8>", "vector", "uint16_t", 8, [])
    type_dic["sycl::vec<uint16_t, 8>"] = t_vuint16t_8

    t_vuint16t_16 = argtype("sycl::vec<uint16_t, 16>", "vector", "uint16_t", 16, [])
    type_dic["sycl::vec<uint16_t, 16>"] = t_vuint16t_16

    t_muint16t_2 = argtype("sycl::marray<uint16_t, 2>", "marray", "uint16_t", 2, [])
    type_dic["sycl::marray<uint16_t, 2>"] = t_muint16t_2

    t_muint16t_3 = argtype("sycl::marray<uint16_t, 3>", "marray", "uint16_t", 3, [])
    type_dic["sycl::marray<uint16_t, 3>"] = t_muint16t_3

    t_muint16t_4 = argtype("sycl::marray<uint16_t, 4>", "marray", "uint16_t", 4, [])
    type_dic["sycl::marray<uint16_t, 4>"] = t_muint16t_4

    t_muint16t_5 = argtype("sycl::marray<uint16_t, 5>", "marray", "uint16_t", 5, [])
    type_dic["sycl::marray<uint16_t, 5>"] = t_muint16t_5

    t_muint16t_17 = argtype("sycl::marray<uint16_t, 17>", "marray", "uint16_t", 17, [])
    type_dic["sycl::marray<uint16_t, 17>"] = t_muint16t_17


    t_int32t_0 = argtype("int32_t", "scalar", "int32_t", 1, [])
    type_dic["int32_t"] = t_int32t_0

    t_vint32t_2 = argtype("sycl::vec<int32_t, 2>", "vector", "int32_t", 2, [])
    type_dic["sycl::vec<int32_t, 2>"] = t_vint32t_2

    t_vint32t_3 = argtype("sycl::vec<int32_t, 3>", "vector", "int32_t", 3, [])
    type_dic["sycl::vec<int32_t, 3>"] = t_vint32t_3

    t_vint32t_4 = argtype("sycl::vec<int32_t, 4>", "vector", "int32_t", 4, [])
    type_dic["sycl::vec<int32_t, 4>"] = t_vint32t_4

    t_vint32t_8 = argtype("sycl::vec<int32_t, 8>", "vector", "int32_t", 8, [])
    type_dic["sycl::vec<int32_t, 8>"] = t_vint32t_8

    t_vint32t_16 = argtype("sycl::vec<int32_t, 16>", "vector", "int32_t", 16, [])
    type_dic["sycl::vec<int32_t, 16>"] = t_vint32t_16

    t_mint32t_2 = argtype("sycl::marray<int32_t, 2>", "marray", "int32_t", 2, [])
    type_dic["sycl::marray<int32_t, 2>"] = t_mint32t_2

    t_mint32t_3 = argtype("sycl::marray<int32_t, 3>", "marray", "int32_t", 3, [])
    type_dic["sycl::marray<int32_t, 3>"] = t_mint32t_3

    t_mint32t_4 = argtype("sycl::marray<int32_t, 4>", "marray", "int32_t", 4, [])
    type_dic["sycl::marray<int32_t, 4>"] = t_mint32t_4

    t_mint32t_5 = argtype("sycl::marray<int32_t, 5>", "marray", "int32_t", 5, [])
    type_dic["sycl::marray<int32_t, 5>"] = t_mint32t_5

    t_mint32t_17 = argtype("sycl::marray<int32_t, 17>", "marray", "int32_t", 17, [])
    type_dic["sycl::marray<int32_t, 17>"] = t_mint32t_17


    t_uint32t_0 = argtype("uint32_t", "scalar", "uint32_t", 1, [])
    type_dic["uint32_t"] = t_uint32t_0

    t_vuint32t_2 = argtype("sycl::vec<uint32_t, 2>", "vector", "uint32_t", 2, [])
    type_dic["sycl::vec<uint32_t, 2>"] = t_vuint32t_2

    t_vuint32t_3 = argtype("sycl::vec<uint32_t, 3>", "vector", "uint32_t", 3, [])
    type_dic["sycl::vec<uint32_t, 3>"] = t_vuint32t_3

    t_vuint32t_4 = argtype("sycl::vec<uint32_t, 4>", "vector", "uint32_t", 4, [])
    type_dic["sycl::vec<uint32_t, 4>"] = t_vuint32t_4

    t_vuint32t_8 = argtype("sycl::vec<uint32_t, 8>", "vector", "uint32_t", 8, [])
    type_dic["sycl::vec<uint32_t, 8>"] = t_vuint32t_8

    t_vuint32t_16 = argtype("sycl::vec<uint32_t, 16>", "vector", "uint32_t", 16, [])
    type_dic["sycl::vec<uint32_t, 16>"] = t_vuint32t_16

    t_muint32t_2 = argtype("sycl::marray<uint32_t, 2>", "marray", "uint32_t", 2, [])
    type_dic["sycl::marray<uint32_t, 2>"] = t_muint32t_2

    t_muint32t_3 = argtype("sycl::marray<uint32_t, 3>", "marray", "uint32_t", 3, [])
    type_dic["sycl::marray<uint32_t, 3>"] = t_muint32t_3

    t_muint32t_4 = argtype("sycl::marray<uint32_t, 4>", "marray", "uint32_t", 4, [])
    type_dic["sycl::marray<uint32_t, 4>"] = t_muint32t_4

    t_muint32t_5 = argtype("sycl::marray<uint32_t, 5>", "marray", "uint32_t", 5, [])
    type_dic["sycl::marray<uint32_t, 5>"] = t_muint32t_5

    t_muint32t_17 = argtype("sycl::marray<uint32_t, 17>", "marray", "uint32_t", 17, [])
    type_dic["sycl::marray<uint32_t, 17>"] = t_muint32t_17


    t_int64t_0 = argtype("int64_t", "scalar", "int64_t", 1, [])
    type_dic["int64_t"] = t_int64t_0

    t_vint64t_2 = argtype("sycl::vec<int64_t, 2>", "vector", "int64_t", 2, [])
    type_dic["sycl::vec<int64_t, 2>"] = t_vint64t_2

    t_vint64t_3 = argtype("sycl::vec<int64_t, 3>", "vector", "int64_t", 3, [])
    type_dic["sycl::vec<int64_t, 3>"] = t_vint64t_3

    t_vint64t_4 = argtype("sycl::vec<int64_t, 4>", "vector", "int64_t", 4, [])
    type_dic["sycl::vec<int64_t, 4>"] = t_vint64t_4

    t_vint64t_8 = argtype("sycl::vec<int64_t, 8>", "vector", "int64_t", 8, [])
    type_dic["sycl::vec<int64_t, 8>"] = t_vint64t_8

    t_vint64t_16 = argtype("sycl::vec<int64_t, 16>", "vector", "int64_t", 16, [])
    type_dic["sycl::vec<int64_t, 16>"] = t_vint64t_16

    t_mint64t_2 = argtype("sycl::marray<int64_t, 2>", "marray", "int64_t", 2, [])
    type_dic["sycl::marray<int64_t, 2>"] = t_mint64t_2

    t_mint64t_3 = argtype("sycl::marray<int64_t, 3>", "marray", "int64_t", 3, [])
    type_dic["sycl::marray<int64_t, 3>"] = t_mint64t_3

    t_mint64t_4 = argtype("sycl::marray<int64_t, 4>", "marray", "int64_t", 4, [])
    type_dic["sycl::marray<int64_t, 4>"] = t_mint64t_4

    t_mint64t_5 = argtype("sycl::marray<int64_t, 5>", "marray", "int64_t", 5, [])
    type_dic["sycl::marray<int64_t, 5>"] = t_mint64t_5

    t_mint64t_17 = argtype("sycl::marray<int64_t, 17>", "marray", "int64_t", 17, [])
    type_dic["sycl::marray<int64_t, 17>"] = t_mint64t_17


    t_uint64t_0 = argtype("uint64_t", "scalar", "uint64_t", 1, [])
    type_dic["uint64_t"] = t_uint64t_0

    t_vuint64t_2 = argtype("sycl::vec<uint64_t, 2>", "vector", "uint64_t", 2, [])
    type_dic["sycl::vec<uint64_t, 2>"] = t_vuint64t_2

    t_vuint64t_3 = argtype("sycl::vec<uint64_t, 3>", "vector", "uint64_t", 3, [])
    type_dic["sycl::vec<uint64_t, 3>"] = t_vuint64t_3

    t_vuint64t_4 = argtype("sycl::vec<uint64_t, 4>", "vector", "uint64_t", 4, [])
    type_dic["sycl::vec<uint64_t, 4>"] = t_vuint64t_4

    t_vuint64t_8 = argtype("sycl::vec<uint64_t, 8>", "vector", "uint64_t", 8, [])
    type_dic["sycl::vec<uint64_t, 8>"] = t_vuint64t_8

    t_vuint64t_16 = argtype("sycl::vec<uint64_t, 16>", "vector", "uint64_t", 16, [])
    type_dic["sycl::vec<uint64_t, 16>"] = t_vuint64t_16

    t_muint64t_2 = argtype("sycl::marray<uint64_t, 2>", "marray", "uint64_t", 2, [])
    type_dic["sycl::marray<uint64_t, 2>"] = t_muint64t_2

    t_muint64t_3 = argtype("sycl::marray<uint64_t, 3>", "marray", "uint64_t", 3, [])
    type_dic["sycl::marray<uint64_t, 3>"] = t_muint64t_3

    t_muint64t_4 = argtype("sycl::marray<uint64_t, 4>", "marray", "uint64_t", 4, [])
    type_dic["sycl::marray<uint64_t, 4>"] = t_muint64t_4

    t_muint64t_5 = argtype("sycl::marray<uint64_t, 5>", "marray", "uint64_t", 5, [])
    type_dic["sycl::marray<uint64_t, 5>"] = t_muint64t_5

    t_muint64t_17 = argtype("sycl::marray<uint64_t, 17>", "marray", "uint64_t", 17, [])
    type_dic["sycl::marray<uint64_t, 17>"] = t_muint64t_17


    # Aliases

    t_float_2 = argtype("sycl::float2", "vector", "float", 2, [])
    type_dic["sycl::float2"] = t_float_2

    t_float_3 = argtype("sycl::float3", "vector", "float", 3, [])
    type_dic["sycl::float3"] = t_float_3

    t_float_4 = argtype("sycl::float4", "vector", "float", 4, [])
    type_dic["sycl::float4"] = t_float_4

    t_float_8 = argtype("sycl::float8", "vector", "float", 8, [])
    type_dic["sycl::float8"] = t_float_8

    t_float_16 = argtype("sycl::float16", "vector", "float", 16, [])
    type_dic["sycl::float16"] = t_float_16


    t_double_2 = argtype("sycl::double2", "vector", "double", 2, [])
    type_dic["sycl::double2"] = t_double_2

    t_double_3 = argtype("sycl::double3", "vector", "double", 3, [])
    type_dic["sycl::double3"] = t_double_3

    t_double_4 = argtype("sycl::double4", "vector", "double", 4, [])
    type_dic["sycl::double4"] = t_double_4

    t_double_8 = argtype("sycl::double8", "vector", "double", 8, [])
    type_dic["sycl::double8"] = t_double_8

    t_double_16 = argtype("sycl::double16", "vector", "double", 16, [])
    type_dic["sycl::double16"] = t_double_16


    t_half_2 = argtype("sycl::half2", "vector", "sycl::half", 2, [])
    type_dic["sycl::half2"] = t_half_2

    t_half_3 = argtype("sycl::half3", "vector", "sycl::half", 3, [])
    type_dic["sycl::half3"] = t_half_3

    t_half_4 = argtype("sycl::half4", "vector", "sycl::half", 4, [])
    type_dic["sycl::half4"] = t_half_4

    t_half_8 = argtype("sycl::half8", "vector", "sycl::half", 8, [])
    type_dic["sycl::half8"] = t_half_8

    t_half_16 = argtype("sycl::half16", "vector", "sycl::half", 16, [])
    type_dic["sycl::half16"] = t_half_16


    t_char_2 = argtype("sycl::char2", "vector", "int8_t", 2, [])
    type_dic["sycl::char2"] = t_char_2

    t_char_3 = argtype("sycl::char3", "vector", "int8_t", 3, [])
    type_dic["sycl::char3"] = t_char_3

    t_char_4 = argtype("sycl::char4", "vector", "int8_t", 4, [])
    type_dic["sycl::char4"] = t_char_4

    t_char_8 = argtype("sycl::char8", "vector", "int8_t", 8, [])
    type_dic["sycl::char8"] = t_char_8

    t_char_16 = argtype("sycl::char16", "vector", "int8_t", 16, [])
    type_dic["sycl::char16"] = t_char_16


    t_uchar_2 = argtype("sycl::uchar2", "vector", "uint8_t", 2, [])
    type_dic["sycl::uchar2"] = t_uchar_2

    t_uchar_3 = argtype("sycl::uchar3", "vector", "uint8_t", 3, [])
    type_dic["sycl::uchar3"] = t_uchar_3

    t_uchar_4 = argtype("sycl::uchar4", "vector", "uint8_t", 4, [])
    type_dic["sycl::uchar4"] = t_uchar_4

    t_uchar_8 = argtype("sycl::uchar8", "vector", "uint8_t", 8, [])
    type_dic["sycl::uchar8"] = t_uchar_8

    t_uchar_16 = argtype("sycl::uchar16", "vector", "uint8_t", 16, [])
    type_dic["sycl::uchar16"] = t_uchar_16


    t_short_2 = argtype("sycl::short2", "vector", "int16_t", 2, [])
    type_dic["sycl::short2"] = t_short_2

    t_short_3 = argtype("sycl::short3", "vector", "int16_t", 3, [])
    type_dic["sycl::short3"] = t_short_3

    t_short_4 = argtype("sycl::short4", "vector", "int16_t", 4, [])
    type_dic["sycl::short4"] = t_short_4

    t_short_8 = argtype("sycl::short8", "vector", "int16_t", 8, [])
    type_dic["sycl::short8"] = t_short_8

    t_short_16 = argtype("sycl::short16", "vector", "int16_t", 16, [])
    type_dic["sycl::short16"] = t_short_16


    t_ushort_2 = argtype("sycl::ushort2", "vector", "uint16_t", 2, [])
    type_dic["sycl::ushort2"] = t_ushort_2

    t_ushort_3 = argtype("sycl::ushort3", "vector", "uint16_t", 3, [])
    type_dic["sycl::ushort3"] = t_ushort_3

    t_ushort_4 = argtype("sycl::ushort4", "vector", "uint16_t", 4, [])
    type_dic["sycl::ushort4"] = t_ushort_4

    t_ushort_8 = argtype("sycl::ushort8", "vector", "uint16_t", 8, [])
    type_dic["sycl::ushort8"] = t_ushort_8

    t_ushort_16 = argtype("sycl::ushort16", "vector", "uint16_t", 16, [])
    type_dic["sycl::ushort16"] = t_ushort_16


    t_int_2 = argtype("sycl::int2", "vector", "int32_t", 2, [])
    type_dic["sycl::int2"] = t_int_2

    t_int_3 = argtype("sycl::int3", "vector", "int32_t", 3, [])
    type_dic["sycl::int3"] = t_int_3

    t_int_4 = argtype("sycl::int4", "vector", "int32_t", 4, [])
    type_dic["sycl::int4"] = t_int_4

    t_int_8 = argtype("sycl::int8", "vector", "int32_t", 8, [])
    type_dic["sycl::int8"] = t_int_8

    t_int_16 = argtype("sycl::int16", "vector", "int32_t", 16, [])
    type_dic["sycl::int16"] = t_int_16


    t_uint_2 = argtype("sycl::uint2", "vector", "uint32_t", 2, [])
    type_dic["sycl::uint2"] = t_uint_2

    t_uint_3 = argtype("sycl::uint3", "vector", "uint32_t", 3, [])
    type_dic["sycl::uint3"] = t_uint_3

    t_uint_4 = argtype("sycl::uint4", "vector", "uint32_t", 4, [])
    type_dic["sycl::uint4"] = t_uint_4

    t_uint_8 = argtype("sycl::uint8", "vector", "uint32_t", 8, [])
    type_dic["sycl::uint8"] = t_uint_8

    t_uint_16 = argtype("sycl::uint16", "vector", "uint32_t", 16, [])
    type_dic["sycl::uint16"] = t_uint_16


    t_long_2 = argtype("sycl::long2", "vector", "int64_t", 2, [])
    type_dic["sycl::long2"] = t_long_2

    t_long_3 = argtype("sycl::long3", "vector", "int64_t", 3, [])
    type_dic["sycl::long3"] = t_long_3

    t_long_4 = argtype("sycl::long4", "vector", "int64_t", 4, [])
    type_dic["sycl::long4"] = t_long_4

    t_long_8 = argtype("sycl::long8", "vector", "int64_t", 8, [])
    type_dic["sycl::long8"] = t_long_8

    t_long_16 = argtype("sycl::long16", "vector", "int64_t", 16, [])
    type_dic["sycl::long16"] = t_long_16


    t_ulong_2 = argtype("sycl::ulong2", "vector", "uint64_t", 2, [])
    type_dic["sycl::ulong2"] = t_ulong_2

    t_ulong_3 = argtype("sycl::ulong3", "vector", "uint64_t", 3, [])
    type_dic["sycl::ulong3"] = t_ulong_3

    t_ulong_4 = argtype("sycl::ulong4", "vector", "uint64_t", 4, [])
    type_dic["sycl::ulong4"] = t_ulong_4

    t_ulong_8 = argtype("sycl::ulong8", "vector", "uint64_t", 8, [])
    type_dic["sycl::ulong8"] = t_ulong_8

    t_ulong_16 = argtype("sycl::ulong16", "vector", "uint64_t", 16, [])
    type_dic["sycl::ulong16"] = t_ulong_16

    return type_dic


    # Generic Types
def create_types():
    type_dic = create_basic_types()

    t_vfloat_n = argtype("vfloatn", "NULL", "NULL", 0, ["sycl::float2","sycl::float3","sycl::float4","sycl::float8","sycl::float16"])
    type_dic["vfloatn"] = t_vfloat_n

    t_mfloat_n = argtype("mfloatn", "NULL", "NULL", 0, ["sycl::marray<float, 2>","sycl::marray<float, 3>","sycl::marray<float, 4>","sycl::marray<float, 5>","sycl::marray<float, 17>"])
    type_dic["mfloatn"] = t_mfloat_n

    t_float_n = argtype("floatn", "NULL", "NULL", 0, ["vfloatn","mfloatn"])
    type_dic["floatn"] = t_float_n


    t_gen_float_f = argtype("genfloatf", "NULL", "NULL", 0, ["float", "floatn"])
    type_dic["genfloatf"] = t_gen_float_f


    t_vdouble_n = argtype("vdoublen", "NULL", "NULL", 0, ["sycl::double2","sycl::double3","sycl::double4","sycl::double8","sycl::double16"])
    type_dic["vdoublen"] = t_vdouble_n

    t_mdouble_n = argtype("mdoublen", "NULL", "NULL", 0, ["sycl::marray<double, 2>","sycl::marray<double, 3>","sycl::marray<double, 4>","sycl::marray<double, 5>","sycl::marray<double, 17>"])
    type_dic["mdoublen"] = t_mdouble_n

    t_double_n = argtype("doublen", "NULL", "NULL", 0, ["vdoublen","mdoublen"])
    type_dic["doublen"] = t_double_n


    t_gen_float_d = argtype("genfloatd", "NULL", "NULL", 0, ["double","doublen"])
    type_dic["genfloatd"] = t_gen_float_d


    t_vhalf_n = argtype("vhalfn", "NULL", "NULL", 0, ["sycl::half2","sycl::half3","sycl::half4","sycl::half8","sycl::half16"])
    type_dic["vhalfn"] = t_vhalf_n

    t_mhalf_n = argtype("mhalfn", "NULL", "NULL", 0, ["sycl::marray<sycl::half, 2>","sycl::marray<sycl::half, 3>","sycl::marray<sycl::half, 4>","sycl::marray<sycl::half, 5>","sycl::marray<sycl::half, 17>"])
    type_dic["mhalfn"] = t_mhalf_n

    t_half_n = argtype("halfn", "NULL", "NULL", 0, ["vhalfn","mhalfn"])
    type_dic["halfn"] = t_half_n


    t_gen_float_h = argtype("genfloath", "NULL", "NULL", 0, ["sycl::half","halfn"])
    type_dic["genfloath"] = t_gen_float_h


    t_gen_float = argtype("genfloat", "NULL", "NULL", 0, ["genfloatf","genfloatd","genfloath"])
    type_dic["genfloat"] = t_gen_float

    t_sgen_float = argtype("sgenfloat", "NULL", "NULL", 0, ["float","double","sycl::half"])
    type_dic["sgenfloat"] = t_sgen_float


    t_gen_geofloat = argtype("gengeofloat", "NULL", "NULL", 0, ["float","sycl::float2","sycl::float3","sycl::float4","sycl::marray<float, 2>","sycl::marray<float, 3>","sycl::marray<float, 4>"])
    type_dic["gengeofloat"] = t_gen_geofloat

    t_gen_geodouble = argtype("gengeodouble", "NULL", "NULL", 0, ["double","sycl::double2","sycl::double3","sycl::double4","sycl::marray<double, 2>","sycl::marray<double, 3>","sycl::marray<double, 4>"])
    type_dic["gengeodouble"] = t_gen_geodouble


    # t_char_n = argtype("charn", "NULL", "NULL", 0, ["sycl::char2","sycl::char3","sycl::char4","sycl::char8","sycl::char16"])
    t_vchar_n = argtype("vcharn", "NULL", "NULL", 0, ["sycl::vec<char, 2>","sycl::vec<char, 3>","sycl::vec<char, 4>","sycl::vec<char, 8>","sycl::vec<char, 16>"])
    type_dic["vcharn"] = t_vchar_n

    t_mchar_n = argtype("mcharn", "NULL", "NULL", 0, ["sycl::marray<char, 2>","sycl::marray<char, 3>","sycl::marray<char, 4>","sycl::marray<char, 5>","sycl::marray<char, 17>"])
    type_dic["mcharn"] = t_mchar_n

    t_char_n = argtype("charn", "NULL", "NULL", 0, ["vcharn", "mcharn"])
    type_dic["charn"] = t_char_n

    # t_schar_n = argtype("scharn", "NULL", "NULL", 0, ["sycl::schar2","sycl::schar3","sycl::schar4","sycl::schar8","sycl::schar16"])
    t_vschar_n = argtype("vscharn", "NULL", "NULL", 0, ["sycl::vec<signed char, 2>","sycl::vec<signed char, 3>","sycl::vec<signed char, 4>","sycl::vec<signed char, 8>","sycl::vec<signed char, 16>"])
    type_dic["vscharn"] = t_vschar_n

    t_mschar_n = argtype("mscharn", "NULL", "NULL", 0, ["sycl::marray<signed char, 2>","sycl::marray<signed char, 3>","sycl::marray<signed char, 4>","sycl::marray<signed char, 5>","sycl::marray<signed char, 17>"])
    type_dic["mscharn"] = t_mschar_n

    t_schar_n = argtype("scharn", "NULL", "NULL", 0, ["vscharn","mscharn"])
    type_dic["scharn"] = t_schar_n

    # t_uchar_n = argtype("ucharn", "NULL", "NULL", 0, ["sycl::uchar2","sycl::uchar3","sycl::uchar4","sycl::uchar8","sycl::uchar16"])
    t_vuchar_n = argtype("vucharn", "NULL", "NULL", 0, ["sycl::vec<unsigned char, 2>","sycl::vec<unsigned char, 3>","sycl::vec<unsigned char, 4>","sycl::vec<unsigned char, 8>","sycl::vec<unsigned char, 16>"])
    type_dic["vucharn"] = t_vuchar_n

    t_muchar_n = argtype("mucharn", "NULL", "NULL", 0, ["sycl::marray<unsigned char, 2>","sycl::marray<unsigned char, 3>","sycl::marray<unsigned char, 4>","sycl::marray<unsigned char, 5>","sycl::marray<unsigned char, 17>"])
    type_dic["mucharn"] = t_muchar_n

    t_uchar_n = argtype("ucharn", "NULL", "NULL", 0, ["vucharn", "mucharn"])
    type_dic["ucharn"] = t_uchar_n


    t_igen_char = argtype("igenchar", "NULL", "NULL", 0, ["signed char","scharn"])
    type_dic["igenchar"] = t_igen_char

    t_ugen_char = argtype("ugenchar", "NULL", "NULL", 0, ["unsigned char","ucharn"])
    type_dic["ugenchar"] = t_ugen_char

    t_gen_char = argtype("genchar", "NULL", "NULL", 0, ["char","charn","igenchar","ugenchar"])
    type_dic["genchar"] = t_gen_char


    # t_short_n = argtype("shortn", "NULL", "NULL", 0, ["sycl::short2","sycl::short3","sycl::short4","sycl::short8","sycl::short16"])
    t_vshort_n = argtype("vshortn", "NULL", "NULL", 0, ["sycl::vec<short, 2>","sycl::vec<short, 3>","sycl::vec<short, 4>","sycl::vec<short, 8>","sycl::vec<short, 16>"])
    type_dic["vshortn"] = t_vshort_n

    t_mshort_n = argtype("mshortn", "NULL", "NULL", 0, ["sycl::marray<short, 2>","sycl::marray<short, 3>","sycl::marray<short, 4>","sycl::marray<short, 5>","sycl::marray<short, 17>"])
    type_dic["mshortn"] = t_mshort_n

    t_short_n = argtype("shortn", "NULL", "NULL", 0, ["vshortn","mshortn"])
    type_dic["shortn"] = t_short_n


    t_gen_short = argtype("genshort", "NULL", "NULL", 0, ["short","shortn"])
    type_dic["genshort"] = t_gen_short


    t_vushort_n = argtype("vushortn", "NULL", "NULL", 0, ["sycl::vec<unsigned short, 2>","sycl::vec<unsigned short, 3>","sycl::vec<unsigned short, 4>","sycl::vec<unsigned short, 8>","sycl::vec<unsigned short, 16>"])
    type_dic["vushortn"] = t_vushort_n

    t_mushort_n = argtype("mushortn", "NULL", "NULL", 0, ["sycl::marray<unsigned short, 2>","sycl::marray<unsigned short, 3>","sycl::marray<unsigned short, 4>","sycl::marray<unsigned short, 5>","sycl::marray<unsigned short, 17>"])
    type_dic["mushortn"] = t_mushort_n

    t_ushort_n = argtype("ushortn", "NULL", "NULL", 0, ["vushortn","mushortn"])
    type_dic["ushortn"] = t_ushort_n


    t_ugen_short = argtype("ugenshort", "NULL", "NULL", 0, ["unsigned short","ushortn"])
    type_dic["ugenshort"] = t_ugen_short


    # t_int_n = argtype("intn", "NULL", "NULL", 0, ["sycl::int2","sycl::int3","sycl::int4","sycl::int8","sycl::int16"])
    t_vint_n = argtype("vintn", "NULL", "NULL", 0, ["sycl::vec<int, 2>","sycl::vec<int, 3>","sycl::vec<int, 4>","sycl::vec<int, 8>","sycl::vec<int, 16>"])
    type_dic["vintn"] = t_vint_n

    t_mint_n = argtype("mintn", "NULL", "NULL", 0, ["sycl::marray<int, 2>","sycl::marray<int, 3>","sycl::marray<int, 4>","sycl::marray<int, 5>","sycl::marray<int, 17>"])
    type_dic["mintn"] = t_mint_n

    t_int_n = argtype("intn", "NULL", "NULL", 0, ["vintn","mintn"])
    type_dic["intn"] = t_int_n


    t_gen_int = argtype("genint", "NULL", "NULL", 0, ["int","intn"])
    type_dic["genint"] = t_gen_int


    # t_uint_n = argtype("uintn", "NULL", "NULL", 0, ["sycl::uint2","sycl::uint3","sycl::uint4","sycl::uint8","sycl::uint16"])
    t_vuint_n = argtype("vuintn", "NULL", "NULL", 0, ["sycl::vec<unsigned, 2>","sycl::vec<unsigned, 3>","sycl::vec<unsigned, 4>","sycl::vec<unsigned, 8>","sycl::vec<unsigned, 16>"])
    type_dic["vuintn"] = t_vuint_n

    t_muint_n = argtype("muintn", "NULL", "NULL", 0, ["sycl::marray<unsigned, 2>","sycl::marray<unsigned, 3>","sycl::marray<unsigned, 4>","sycl::marray<unsigned, 5>","sycl::marray<unsigned, 17>"])
    type_dic["muintn"] = t_muint_n

    t_uint_n = argtype("uintn", "NULL", "NULL", 0, ["vuintn","muintn"])
    type_dic["uintn"] = t_uint_n


    t_ugen_int = argtype("ugenint", "NULL", "NULL", 0, ["unsigned","uintn"])
    type_dic["ugenint"] = t_ugen_int


    # t_long_n = argtype("longn", "NULL", "NULL", 0, ["sycl::long2","sycl::long3","sycl::long4","sycl::long8","sycl::long16"])
    t_vlong_n = argtype("vlongn", "NULL", "NULL", 0, ["sycl::vec<long, 2>","sycl::vec<long, 3>","sycl::vec<long, 4>","sycl::vec<long, 8>","sycl::vec<long, 16>"])
    type_dic["vlongn"] = t_vlong_n

    t_mlong_n = argtype("mlongn", "NULL", "NULL", 0, ["sycl::marray<long, 2>","sycl::marray<long, 3>","sycl::marray<long, 4>","sycl::marray<long, 5>","sycl::marray<long, 17>"])
    type_dic["mlongn"] = t_mlong_n

    t_long_n = argtype("longn", "NULL", "NULL", 0, ["vlongn","mlongn"])
    type_dic["longn"] = t_long_n


    t_gen_long = argtype("genlong", "NULL", "NULL", 0, ["long", "longn"])
    type_dic["genlong"] = t_gen_long


    # t_ulong_n = argtype("ulongn", "NULL", "NULL", 0, ["sycl::ulong2","sycl::ulong3","sycl::ulong4","sycl::ulong8","sycl::ulong16"])
    t_vulong_n = argtype("vulongn", "NULL", "NULL", 0, ["sycl::vec<unsigned long, 2>","sycl::vec<unsigned long, 3>","sycl::vec<unsigned long, 4>","sycl::vec<unsigned long, 8>","sycl::vec<unsigned long, 16>"])
    type_dic["vulongn"] = t_vulong_n

    t_mulong_n = argtype("mulongn", "NULL", "NULL", 0, ["sycl::marray<unsigned long, 2>","sycl::marray<unsigned long, 3>","sycl::marray<unsigned long, 4>","sycl::marray<unsigned long, 5>","sycl::marray<unsigned long, 17>"])
    type_dic["mulongn"] = t_mulong_n

    t_ulong_n = argtype("ulongn", "NULL", "NULL", 0, ["vulongn","mulongn"])
    type_dic["ulongn"] = t_ulong_n


    t_ugen_long = argtype("ugenlong", "NULL", "NULL", 0, ["unsigned long", "ulongn"])
    type_dic["ugenlong"] = t_ugen_long


    # t_longlong_n = argtype("longlongn", "NULL", "NULL", 0, ["sycl::longlong2","sycl::longlong3","sycl::longlong4","sycl::longlong8","sycl::longlong16"])
    t_vlonglong_n = argtype("vlonglongn", "NULL", "NULL", 0, ["sycl::vec<long long, 2>","sycl::vec<long long, 3>","sycl::vec<long long, 4>","sycl::vec<long long, 8>","sycl::vec<long long, 16>"])
    type_dic["vlonglongn"] = t_vlonglong_n

    t_mlonglong_n = argtype("mlonglongn", "NULL", "NULL", 0, ["sycl::marray<long long, 2>","sycl::marray<long long, 3>","sycl::marray<long long, 4>","sycl::marray<long long, 5>","sycl::marray<long long, 17>"])
    type_dic["mlonglongn"] = t_mlonglong_n

    t_longlong_n = argtype("longlongn", "NULL", "NULL", 0, ["vlonglongn","mlonglongn"])
    type_dic["longlongn"] = t_longlong_n


    t_gen_longlong = argtype("genlonglong", "NULL", "NULL", 0, ["long long", "longlongn"])
    type_dic["genlonglong"] = t_gen_longlong


    # t_ulonglong_n = argtype("ulonglongn", "NULL", "NULL", 0, ["sycl::ulonglong2","sycl::ulonglong3","sycl::ulonglong4","sycl::ulonglong8","sycl::ulonglong16"])
    t_vulonglong_n = argtype("vulonglongn", "NULL", "NULL", 0, ["sycl::vec<unsigned long long, 2>","sycl::vec<unsigned long long, 3>","sycl::vec<unsigned long long, 4>","sycl::vec<unsigned long long, 8>","sycl::vec<unsigned long long, 16>"])
    type_dic["vulonglongn"] = t_vulonglong_n

    t_mulonglong_n = argtype("mulonglongn", "NULL", "NULL", 0, ["sycl::marray<unsigned long long, 2>","sycl::marray<unsigned long long, 3>","sycl::marray<unsigned long long, 4>","sycl::marray<unsigned long long, 5>","sycl::marray<unsigned long long, 17>"])
    type_dic["mulonglongn"] = t_mulonglong_n

    t_ulonglong_n = argtype("ulonglongn", "NULL", "NULL", 0, ["vulonglongn","mulonglongn"])
    type_dic["ulonglongn"] = t_ulonglong_n


    t_ugen_longlong = argtype("ugenlonglong", "NULL", "NULL", 0, ["unsigned long long", "ulonglongn"])
    type_dic["ugenlonglong"] = t_ugen_longlong


    t_igen_long_integer = argtype("igenlonginteger", "NULL", "NULL", 0, ["genlong", "genlonglong"])
    type_dic["igenlonginteger"] = t_igen_long_integer

    t_ugen_long_integer = argtype("ugenlonginteger", "NULL", "NULL", 0, ["ugenlong", "ugenlonglong"])
    type_dic["ugenlonginteger"] = t_ugen_long_integer


    # Fixed size generic types

    t_vigen_integer_8bit = argtype("vigeninteger8bit", "NULL", "NULL", 0, ["sycl::vec<int8_t, 2>","sycl::vec<int8_t, 3>","sycl::vec<int8_t, 4>","sycl::vec<int8_t, 8>","sycl::vec<int8_t, 16>"])
    type_dic["vigeninteger8bit"] = t_vigen_integer_8bit

    t_migen_integer_8bit = argtype("migeninteger8bit", "NULL", "NULL", 0, ["sycl::marray<int8_t, 2>","sycl::marray<int8_t, 3>","sycl::marray<int8_t, 4>","sycl::marray<int8_t, 5>","sycl::marray<int8_t, 17>"])
    type_dic["migeninteger8bit"] = t_migen_integer_8bit

    t_igen_integer_8bit = argtype("igeninteger8bit", "NULL", "NULL", 0, ["int8_t","vigeninteger8bit","migeninteger8bit"])
    type_dic["igeninteger8bit"] = t_igen_integer_8bit


    t_vugen_integer_8bit = argtype("vugeninteger8bit", "NULL", "NULL", 0, ["sycl::vec<uint8_t, 2>","sycl::vec<uint8_t, 3>","sycl::vec<uint8_t, 4>","sycl::vec<uint8_t, 8>","sycl::vec<uint8_t, 16>"])
    type_dic["vugeninteger8bit"] = t_vugen_integer_8bit

    t_mugen_integer_8bit = argtype("mugeninteger8bit", "NULL", "NULL", 0, ["sycl::marray<uint8_t, 2>","sycl::marray<uint8_t, 3>","sycl::marray<uint8_t, 4>","sycl::marray<uint8_t, 5>","sycl::marray<uint8_t, 17>"])
    type_dic["mugeninteger8bit"] = t_mugen_integer_8bit

    t_ugen_integer_8bit = argtype("ugeninteger8bit", "NULL", "NULL", 0, ["uint8_t","vugeninteger8bit","mugeninteger8bit"])
    type_dic["ugeninteger8bit"] = t_ugen_integer_8bit


    t_gen_integer_8bit = argtype("geninteger8bit", "NULL", "NULL", 0, ["igeninteger8bit","ugeninteger8bit"])
    type_dic["geninteger8bit"] = t_gen_integer_8bit


    t_vigen_integer_16bit = argtype("vigeninteger16bit", "NULL", "NULL", 0, ["sycl::vec<int16_t, 2>","sycl::vec<int16_t, 3>","sycl::vec<int16_t, 4>","sycl::vec<int16_t, 8>","sycl::vec<int16_t, 16>"])
    type_dic["vigeninteger16bit"] = t_vigen_integer_16bit

    t_migen_integer_16bit = argtype("migeninteger16bit", "NULL", "NULL", 0, ["sycl::marray<int16_t, 2>","sycl::marray<int16_t, 3>","sycl::marray<int16_t, 4>","sycl::marray<int16_t, 5>","sycl::marray<int16_t, 17>"])
    type_dic["migeninteger16bit"] = t_migen_integer_16bit

    t_igen_integer_16bit = argtype("igeninteger16bit", "NULL", "NULL", 0, ["vigeninteger16bit","migeninteger16bit"])
    type_dic["igeninteger16bit"] = t_igen_integer_16bit


    t_vugen_integer_16bit = argtype("vugeninteger16bit", "NULL", "NULL", 0, ["sycl::vec<uint16_t, 2>","sycl::vec<uint16_t, 3>","sycl::vec<uint16_t, 4>","sycl::vec<uint16_t, 8>","sycl::vec<uint16_t, 16>"])
    type_dic["vugeninteger16bit"] = t_vugen_integer_16bit

    t_mugen_integer_16bit = argtype("mugeninteger16bit", "NULL", "NULL", 0, ["sycl::marray<uint16_t, 2>","sycl::marray<uint16_t, 3>","sycl::marray<uint16_t, 4>","sycl::marray<uint16_t, 5>","sycl::marray<uint16_t, 17>"])
    type_dic["mugeninteger16bit"] = t_mugen_integer_16bit

    t_ugen_integer_16bit = argtype("ugeninteger16bit", "NULL", "NULL", 0, ["vugeninteger16bit","mugeninteger16bit"])
    type_dic["ugeninteger16bit"] = t_ugen_integer_16bit


    t_gen_integer_16bit = argtype("geninteger16bit", "NULL", "NULL", 0, ["igeninteger16bit","ugeninteger16bit"])
    type_dic["geninteger16bit"] = t_gen_integer_16bit


    t_vigen_integer_32bit = argtype("vigeninteger32bit", "NULL", "NULL", 0, ["sycl::vec<int32_t, 2>","sycl::vec<int32_t, 3>","sycl::vec<int32_t, 4>","sycl::vec<int32_t, 8>","sycl::vec<int32_t, 16>"])
    type_dic["vigeninteger32bit"] = t_vigen_integer_32bit

    t_migen_integer_32bit = argtype("migeninteger32bit", "NULL", "NULL", 0, ["sycl::marray<int32_t, 2>","sycl::marray<int32_t, 3>","sycl::marray<int32_t, 4>","sycl::marray<int32_t, 5>","sycl::marray<int32_t, 17>"])
    type_dic["migeninteger32bit"] = t_migen_integer_32bit

    t_igen_integer_32bit = argtype("igeninteger32bit", "NULL", "NULL", 0, ["vigeninteger32bit","migeninteger32bit"])
    type_dic["igeninteger32bit"] = t_igen_integer_32bit


    t_vugen_integer_32bit = argtype("vugeninteger32bit", "NULL", "NULL", 0, ["sycl::vec<uint32_t, 2>","sycl::vec<uint32_t, 3>","sycl::vec<uint32_t, 4>","sycl::vec<uint32_t, 8>","sycl::vec<uint32_t, 16>"])
    type_dic["vugeninteger32bit"] = t_vugen_integer_32bit

    t_mugen_integer_32bit = argtype("mugeninteger32bit", "NULL", "NULL", 0, ["sycl::marray<uint32_t, 2>","sycl::marray<uint32_t, 3>","sycl::marray<uint32_t, 4>","sycl::marray<uint32_t, 5>","sycl::marray<uint32_t, 17>"])
    type_dic["mugeninteger32bit"] = t_mugen_integer_32bit

    t_ugen_integer_32bit = argtype("ugeninteger32bit", "NULL", "NULL", 0, ["vugeninteger32bit","mugeninteger32bit"])
    type_dic["ugeninteger32bit"] = t_ugen_integer_32bit


    t_gen_integer_32bit = argtype("geninteger32bit", "NULL", "NULL", 0, ["igeninteger32bit","ugeninteger32bit"])
    type_dic["geninteger32bit"] = t_gen_integer_32bit


    t_vigen_integer_64bit = argtype("vigeninteger64bit", "NULL", "NULL", 0, ["sycl::vec<int64_t, 2>","sycl::vec<int64_t, 3>","sycl::vec<int64_t, 4>","sycl::vec<int64_t, 8>","sycl::vec<int64_t, 16>"])
    type_dic["vigeninteger64bit"] = t_vigen_integer_64bit

    t_migen_integer_64bit = argtype("migeninteger64bit", "NULL", "NULL", 0, ["sycl::marray<int64_t, 2>","sycl::marray<int64_t, 3>","sycl::marray<int64_t, 4>","sycl::marray<int64_t, 5>","sycl::marray<int64_t, 17>"])
    type_dic["migeninteger64bit"] = t_migen_integer_64bit

    t_igen_integer_64bit = argtype("igeninteger64bit", "NULL", "NULL", 0, ["vigeninteger64bit","migeninteger64bit"])
    type_dic["igeninteger64bit"] = t_igen_integer_64bit


    t_vugen_integer_64bit = argtype("vugeninteger64bit", "NULL", "NULL", 0, ["sycl::vec<uint64_t, 2>","sycl::vec<uint64_t, 3>","sycl::vec<uint64_t, 4>","sycl::vec<uint64_t, 8>","sycl::vec<uint64_t, 16>"])
    type_dic["vugeninteger64bit"] = t_vugen_integer_64bit

    t_mugen_integer_64bit = argtype("mugeninteger64bit", "NULL", "NULL", 0, ["sycl::marray<uint64_t, 2>","sycl::marray<uint64_t, 3>","sycl::marray<uint64_t, 4>","sycl::marray<uint64_t, 5>","sycl::marray<uint64_t, 17>"])
    type_dic["mugeninteger64bit"] = t_mugen_integer_64bit

    t_ugen_integer_64bit = argtype("ugeninteger64bit", "NULL", "NULL", 0, ["vugeninteger64bit","mugeninteger64bit"])
    type_dic["ugeninteger64bit"] = t_ugen_integer_64bit


    t_gen_integer_64bit = argtype("geninteger64bit", "NULL", "NULL", 0, ["igeninteger64bit","ugeninteger64bit"])
    type_dic["geninteger64bit"] = t_gen_integer_64bit


    # Full generic types

    t_gen_integer = argtype("geninteger", "NULL", "NULL", 0, ["genchar","genshort","ugenshort","genint","ugenint","igenlonginteger","ugenlonginteger",
                                                              "geninteger8bit","geninteger16bit","geninteger32bit","geninteger64bit"])
    type_dic["geninteger"] = t_gen_integer

    t_igen_integer = argtype("igeninteger", "NULL", "NULL", 0, ["igenchar","genshort","genint","igenlonginteger",
                                                                "igeninteger8bit","igeninteger16bit","igeninteger32bit","igeninteger64bit"])
    type_dic["igeninteger"] = t_igen_integer

    t_ugen_integer = argtype("ugeninteger", "NULL", "NULL", 0, ["ugenchar","ugenshort","ugenint","ugenlonginteger",
                                                                "ugeninteger8bit","ugeninteger16bit","ugeninteger32bit","ugeninteger64bit"])
    type_dic["ugeninteger"] = t_ugen_integer


    t_sigen_integer = argtype("sigeninteger", "NULL", "NULL", 0, ["signed char","short","int","long","long long",
                                                                  "int8_t","int16_t","int32_t","int64_t"])
    type_dic["sigeninteger"] = t_sigen_integer

    t_sugen_integer = argtype("sugeninteger", "NULL", "NULL", 0, ["unsigned char","unsigned short","unsigned","unsigned long","unsigned long long",
                                                                  "uint8_t","uint16_t","uint32_t","uint64_t"])
    type_dic["sugeninteger"] = t_sugen_integer

    t_sgen_integer = argtype("sgeninteger", "NULL", "NULL", 0, ["char","sigeninteger","sugeninteger"])
    type_dic["sgeninteger"] = t_sgen_integer


    t_sgen_type = argtype("sgentype", "NULL", "NULL", 0, ["sgenfloat", "sgeninteger"])
    type_dic["sgentype"] = t_sgen_type


    t_vgenfloat_type = argtype("vgenfloat", "NULL", "NULL", 0, ["sycl::vec<float, 2>","sycl::vec<float, 3>","sycl::vec<float, 4>","sycl::vec<float, 8>","sycl::vec<float, 16>",
                                                                "sycl::vec<double, 2>","sycl::vec<double, 3>","sycl::vec<double, 4>","sycl::vec<double, 8>","sycl::vec<double, 16>",
                                                                "sycl::vec<sycl::half, 2>","sycl::vec<sycl::half, 3>","sycl::vec<sycl::half, 4>","sycl::vec<sycl::half, 8>","sycl::vec<sycl::half, 16>"])
    type_dic["vgenfloat"] = t_vgenfloat_type

    t_mgenfloat_type = argtype("mgenfloat", "NULL", "NULL", 0, ["sycl::marray<float, 2>","sycl::marray<float, 3>","sycl::marray<float, 4>","sycl::marray<float, 5>","sycl::marray<float, 17>",
                                                                "sycl::marray<double, 2>","sycl::marray<double, 3>","sycl::marray<double, 4>","sycl::marray<double, 5>","sycl::marray<double, 17>",
                                                                "sycl::marray<sycl::half, 2>","sycl::marray<sycl::half, 3>","sycl::marray<sycl::half, 4>","sycl::marray<sycl::half, 5>","sycl::marray<sycl::half, 17>"])
    type_dic["mgenfloat"] = t_mgenfloat_type


    t_vigeninteger_type = argtype("vigeninteger", "NULL", "NULL", 0, ["vscharn", "vshortn", "vintn", "vlongn", "vlonglongn", "vigeninteger8bit", "vigeninteger16bit", "vigeninteger32bit", "vigeninteger64bit"])
    type_dic["vigeninteger"] = t_vigeninteger_type

    t_migeninteger_type = argtype("migeninteger", "NULL", "NULL", 0, ["mscharn", "mshortn", "mintn", "mlongn", "mlonglongn", "migeninteger8bit", "migeninteger16bit", "migeninteger32bit", "migeninteger64bit"])
    type_dic["migeninteger"] = t_migeninteger_type


    t_vugeninteger_type = argtype("vugeninteger", "NULL", "NULL", 0, ["vucharn", "vushortn", "vuintn", "vulongn", "vulonglongn", "vugeninteger8bit", "vugeninteger16bit", "vugeninteger32bit", "vugeninteger64bit"])
    type_dic["vugeninteger"] = t_vugeninteger_type

    t_mugeninteger_type = argtype("mugeninteger", "NULL", "NULL", 0, ["mucharn", "mushortn", "muintn", "mulongn", "mulonglongn", "mugeninteger8bit", "mugeninteger16bit", "mugeninteger32bit", "mugeninteger64bit"])
    type_dic["mugeninteger"] = t_mugeninteger_type


    t_vgeninteger_type = argtype("vgeninteger", "NULL", "NULL", 0, ["vcharn", "vigeninteger", "vugeninteger"])
    type_dic["vgeninteger"] = t_vgeninteger_type

    t_mgeninteger_type = argtype("mgeninteger", "NULL", "NULL", 0, ["mcharn", "migeninteger", "mugeninteger"])
    type_dic["mgeninteger"] = t_mgeninteger_type


    t_vgen_type = argtype("vgentype", "NULL", "NULL", 0, ["vgenfloat", "vgeninteger"])
    type_dic["vgentype"] = t_vgen_type

    t_mgen_type = argtype("mgentype", "NULL", "NULL", 0, ["mgenfloat", "mgeninteger"])
    type_dic["mgentype"] = t_mgen_type


    t_gen_type = argtype("gentype", "NULL", "NULL", 0, ["genfloat", "geninteger"])
    type_dic["gentype"] = t_gen_type

    return type_dic
