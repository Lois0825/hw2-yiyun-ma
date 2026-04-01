
## Issue Encountered

During development, I initially used the model "gemini-pro", but it resulted in an error.

The error message indicated that the model was not available for the API version.


![alt text](<截屏2026-04-01 17.16.45.png>)

## Fix

I changed the model to "gemini-1.5-flash", which is supported.

After this change, the system worked correctly and was able to generate outputs.

## Reflection

This showed that model selection matters, and not all models are available in the same API version.
Added after testing

