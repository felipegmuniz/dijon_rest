# Dijon & Beaune Lead Mapping Tool

**Author**: Felipe G. Muniz &#x20;
**Residency**: France &#x20;
**Project Start**: July 2024 &#x20;
**Last Updated**: 2025 &#x20;
**Contact**: [felipegmuniz.github.io](https://felipegmuniz.github.io)

## Project Overview

This project is a geo-visualization and lead qualification tool designed for sales and marketing teams working in the food equipment sector, particularly for ITW-FEG products. The regions of **Dijon** and **Beaune** in France were selected as a pilot area to map potential B2B leads such as:

* **Restaurants**
* **EHPADs** (retirement homes)
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
MIT License with Attribution Requirement

Copyright (c) 2025 Felipe G. Muniz

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software. Attribution to the original
author (Felipe G. Muniz) must be maintained in all derived works, including
internal use and commercial adaptations.

Any distribution or modification of this project for public or private use,
in France or internationally, must retain full authorship credit and include
this licensing statement.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
```

## Deployment

The project is live at: &#x20;
👉 [https://felipegmuniz.github.io/dijon\_rest/index.html](https://felipegmuniz.github.io/dijon_rest/index.html)

---

**Note**: This project is designed for internal use and CRM enhancement. Unauthorized reuse, reproduction, or modification without proper attribution is strictly prohibited under international copyright protection.
