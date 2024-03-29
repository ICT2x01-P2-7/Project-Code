Git Workflow
=============

Branches description
--------------------

The **master** branch is where stable code is being store. A stable code is code that has been confirmed to be working.
The **develop** branch is where collaborative development work is done. Code here is considered unstable and may crash. Pull requests are always made to this branch.
Other branches are **development** branches. These branches correspond to each team member and is where each team member works on their feature. These branches are named **<NameOfMember>Branch**.

How to use Git on the project
-----------------------------

- After a pull request has been approved and merged, merge develop into your branch

```git checkout <NameOfMember>Branch```
```git merge develop```

- Resolve any conflicts if any
- Commit your modifications on it
- Push your changes to your branches

```git push```

- Open a Pull Request **to the develop branch**
- Once a reviewer has reviewed and approved the Pull Request, your changes will be squashed into a single commit and merged into the develop branch.
- Note: DO NOT DELETE your branch as the commits are needed for accounting purposes.
- Repeat the above steps for the next feature.

**NOTE**: Do not merge your development branch on **master** and **develop** otherwise you will merge not validated features! Always open Pull Requests from your branch to **develop** after a feature is completed.

Tags and Releases
------------------

The latest commit on the last day of the week will be pushed to master and tagged as the weekly release after testing.
  
Workflow Diagram
------------------
![ICT2201_2101 Project Diagrams - Git Workflow](https://user-images.githubusercontent.com/77475889/143162837-d71af599-fecc-46bb-af38-7505ead28bc8.png)
