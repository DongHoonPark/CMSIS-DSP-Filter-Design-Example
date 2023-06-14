# CMSIS-DSP Filter Design Example

The example describes how the digital iir filter which designed on python scipy can be used on CMSIS-DSP library 

## Background

- [CMSIS-DSP](https://github.com/ARM-software/CMSIS-DSP)
- [SciPy](https://github.com/scipy/scipy)

## Procedure

- Design filter with scipy and get coefficient
- Initialize CMSIS-DSP iir filter with given coefficient
- Emulate CMSIS-DSP step input
- Check step response with scipy pacakge