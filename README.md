### HTML Files

**index.html**:
- Contains the home page where the user can upload an image.
- Includes the necessary form and image upload functionality.

**results.html**:
- Displays the results of the image analysis.
- Lists the type and scope of the project, as well as the needed materials and tools.

### Routes

**`/`**:
- Renders the home page, **index.html**.

**`/analyse_image`**:
- Accepts an image upload via a POST request.
- Analyses the image using a pre-trained model to determine the project details.
- Redirects to **`/results`** with the analysis results.

**`/results`**:
- Renders the results page, **results.html**.
- Receives the analysis results from the `/analyse_image` route.
- Displays the project details, materials, and tools.