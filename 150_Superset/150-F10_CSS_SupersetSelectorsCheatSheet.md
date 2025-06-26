# 

**Setting CSS Variables for Dynamic Styling.**

These provide a way to store values like colors, fonts, or any CSS value under a custom name.

<u>Example: Using variables to define PSF branding colours*.*</u>

*Note: using the **:root** selector makes the variables available throughout the entire document.*

*:root {*

*--psf-dark-blue: \#093059;*

*--inverted-text-color: \#ffffff;*

*--psf-yellow: \#ffd901;*

*--psf-aqua: \#74bdb8;*

*--border-radius: 9px;*

*--psf-beige: \#f8f2e6;*

*--psf-dark-teal: \#0a4b60;*

*}*

<u>Example CSS Variable Reference:</u>

element {

> color: var(-- psf-dark-blue);

}
