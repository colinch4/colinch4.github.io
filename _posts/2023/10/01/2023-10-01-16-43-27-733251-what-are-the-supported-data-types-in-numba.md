---
layout: post
title: "What are the supported data types in Numba?"
description: " "
date: 2023-10-01
tags: [Numba, Python]
comments: true
share: true
---

1. Numeric Data Types:
   - **int8, int16, int32, int64**: Signed integer types with different bit sizes.
   - **uint8, uint16, uint32, uint64**: Unsigned integer types with different bit sizes.
   - **float32, float64**: Single-precision and double-precision floating-point numbers.
   - **complex64, complex128**: Complex numbers with single and double precision.

2. Booleans:
   - **bool**: Represents boolean (True/False) values.

3. Arrays:
   - **int8[:], int16[:], int32[:], int64[:]**: Typed arrays of signed integers with different bit sizes.
   - **float32[:], float64[:]**: Typed arrays of floating-point numbers.
   - **bool[:]**: Typed arrays of boolean values.
   - **complex64[:], complex128[:]**: Typed arrays of complex numbers.

4. Other Types:
   - **void**: Represents no type or void return type.
   - **object**: Generic (Python) object type.

Numba also supports type inference, where it can automatically deduce the data type based on context and usage. This helps in optimizing the generated code further.

#Numba #Python