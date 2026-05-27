# About
Redivis doesn't have the concept of scheduling notebooks to run. This is a bummer for datasets that we want to update with any kind of frequency. It does, however, let you run a notebook via its API. That's what this program does, and it can be used on any notebook.

In the future, whenever Redivis implements scheduled runs, we can hopefully discontinue these — though we'll still need to update the dataset pages in WordPress.

## Usage
1. Fork this repo.

2. Rename the repo following this convention `BUTLER_[name_of_dataset]`. So for the `p_murder_suicides_family_annihilations` dataset it's `BUTLER_p_murder_suicides_family_annihilations`.

3. Change the following variables in the [`get.py`](get.py) file. 
    ```
        username = "[YOUR_USERNAME]"  # Replace with your Redivis username
        workflow_name = "[WORKFLOW_NAME]"  # Replace with your workflow name
        notebook_name = "[NOTEBOOK_NAME]"  # Replace with your notebook name
        wp_post = "[POST_ID]"  # Replace with your WordPress post ID
    ```
    Sticking with the `r_gva` example that would be:
    ```
        username = "TheTrace"  # Replace with your Redivis username
        workflow_name = "immigration_shootings:k6j5"  # Replace with your workflow name
        notebook_name = "updater:5n3r"  # Replace with your notebook name
        wp_post = "1378"  # Replace with your WordPress post ID
    ```
    
    **Where to find**: The URL format for a notebook `https://redivis.com/workflows/k6j5-a1w7z98vq/notebooks/5n3r-0jgwz2mhp` is the easiest way to grab the 'qualified reference' information required after the `:` above. This is the URL grabbed from the `immigration_shootings` workflow with the `updater` notebook selected in the workflow's lefthand tree diagram. The **k6j5** and **5n3r** are what you're after for workflow and notebook names, respectively. The WordPress post ID is found in the URL of the post editor interface for your post; it's the only number in the URL. Here it's **1378** from `https://datahub.thetrace.org/wp-admin/post.php?post=1378&action=edit`.

4. Lastly, set the time that the notebook should run in the [`dataset-butler.yml`](.github/workflows/dataset-butler.yml) file. If you don't wanna think too hard about crontab time formatting here's a [helpful resource](https://crontab.guru/).
    ```
      # schedule: # Uncomment to enable scheduled runs
        # - cron: '0 10 * * *' # Uncomment to enable scheduled runs
    ```

5. Test that it works by clicking the `Actions` button above on the GitHub page. Click `Python application` in the left rail and then click the gray `Run workflow` button in the blue highlighted area.
