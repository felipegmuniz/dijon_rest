# Dijon & Beaune Lead Mapping Tool

**Author**: Felipe G. Muniz &#x20;
**Residency**: France &#x20;
**Project Start**: July 2024 &#x20;
**Last Updated**: 2025 &#x20;
**Contact**: [felipegmuniz.github.io](https://felipegmuniz.github.io)

## Project Overview

This project is a geo-visualization and lead qualification tool designed for sales and marketing teams working in the food equipment sector. The regions of **Dijon** and **Beaune** in France were selected as a pilot area to map potential B2B leads such as:

* **Restaurants**
* **EHPADs** (nursing homes)
* **Schools and Colleges**

The project leverages a filtered dataset and provides an **interactive map** and **heatmap layer** to visually assess geographical lead density and category segmentation.

## Key Features

* **Interactive Folium Map**: Establishments displayed with category-based icons and popups.
* **Heatmap Layer**: Highlights areas with high lead concentration.
* **Custom Popups**: Show name, address, postal code, and category.
* **Category Color Coding**: Different colors for restaurants, rest homes, schools, etc.
* **CRM-Ready**: Dataset is structured for seamless integration with CRM platforms like **Microsoft Dynamics**.

## Usage Goals

* Enable pre-CRM **lead discovery** and prioritization.
* Provide visual **sales intelligence** for field teams.
* Empower sales agents to **update and qualify** leads (future feature).

## Future Enhancements

* Authenticated form-based lead update system.
* Qualification workflow and validation.
* CRM automation with Power Automate or Dynamics 365 API.
* Additional filters and time-based analytics.

## Project Structure

* `create_map.py` – Python code to generate the interactive map and heat layer.
* `dashaboard_generator.py` – Visualization and category distribution comparison.
* `convertLambertWgs84.py` – Coordinate conversion from Lambert-93 to WGS84.
* `index.html` – Final deployed version for GitHub Pages.

## Attribution & Licensing

This project is the intellectual property of **Felipe G. Muniz**, developed in **France**. All rights reserved under applicable international copyright laws.

### License

```
Strict Attribution License (Derived from MIT)

Copyright (c) 2025 Felipe G. Muniz

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, and distribute copies of the Software for
non-commercial purposes, subject to the following conditions:

1. **Attribution is mandatory**: The above copyright notice and this
   permission notice must be included in all copies or substantial portions
   of the Software.

2. **Commercial use is restricted**: Commercial use (including but not limited to resale,
   internal enterprise applications, or integration in proprietary systems)
   requires prior written consent from the author.

3. **Modification control**: Any modification, adaptation, or derivative work
   must clearly identify all changes and retain the original authorship.

4. **Redistribution**: Redistribution is allowed only with full authorship
   credit, license inclusion, and clear notice that the work derives from this
   project.

5. **International enforcement**: This license is governed by French and international
   intellectual property laws. Breach of these conditions may result in legal action.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
```

## Deployment

The project is live at: &#x20;
 [https://felipegmuniz.github.io/dijon\_rest/index.html](https://felipegmuniz.github.io/dijon_rest/index.html)

---

**Note**: This project is designed for internal use and CRM enhancement. Unauthorized reuse, reproduction, modification, or commercial use without prior written consent and proper attribution is strictly prohibited under international copyright protection.
