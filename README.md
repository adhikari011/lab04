# Iterative Exponentiation

## Assigned: Monday, 12 Feb 2024

## Due: Monday, 19 Feb 2024

## Expiration Date: Monday 26 Feb 2024, 2:30pm

## Project Goals

This engineering effort invites you to combine what you learned about the basics of Python programming to implement a program that can use a `for` loop and/or a `while` loop to perform a series of exponentiations (i.e., raising a value to some defined power).

The function that you will implement will repeatedly perform an exponentiation and then save the result of the computation in the list. Ultimately, the output of the program should confirm that it is possible to use either a `for` loop or a `while` loop to produce the same program output.

As you learn more about how to translate mathematical equations into Python functions, you will implement and test a complete Python program while using tools such as the VS Code text editor, a terminal window, and the Poetry package manager.

## Project Access

You can access this assignment by clicking the link provided to you in Discord or in the course schedule. Once you click this link it will create a GitHub repository that you can clone to your computer by using the `git clone` command to download the project from GitHub to your computer. Now you are ready to add source code and documentation to the project!

## Expected Output

This project invites you to implement a program called `iterator`. The program has two flags called `--forloop` and `--whileloop` that control the type of iteration construct with which the program performs iterative exponentiation. To best understand the program's behavior it is nice to observe how it operates when given different command-line arguments. For instance, the command `poetry run iterator --forloop --whileloop --minimum 0 --maximum 2` produces the following output. 

```
Calculating the powers of 2 from 0 to 2 with iteration:

  Should I use a for loop? Yes
  Should I use a while loop? Yes

  Here is the output with the for loop.

   2**0 = 1
   2**1 = 2

  Here is the output with the while loop.

   2**0 = 1
   2**1 = 2

Wow, all of that iteration was exhausting! 😂
```

Can you see the pattern? Please note that the use of both the flags `--forloop` and `--whileloop` means that the program will iteratively compute the powers of two with both a `for` and `while` loop.

It is important to note that the Python program can also produce the output of the powers of two using a single type of iteration construct. For instance, the command `poetry run iterator --forloop --minimum 0 --maximum 5` produces the following output demonstrating that the program only ran a `for` loop. As in the previous output example, this output shows that the program uses the `**` operator to raise `2` to the power of a number such as `0`, `1`, and `2`. Both of these output examples also show that the program should contain several lines of diagnostic output that make it clear how it interpreted the command-line arguments. This output should be made before performing iterative exponentiation.

```
Calculating the powers of 2 from 0 to 5 with iteration:

  Should I use a for loop? Yes
  Should I use a while loop? No

  Here is the output with the for loop.

   2**0 = 1
   2**1 = 2
   2**2 = 4
   2**3 = 8
   2**4 = 16

Wow, all of that iteration was exhausting! 😂
```

While all of the prior examples show that the `iterator` works when you use `0` as the value for the `--minimum`, it is also important to point out that it should work when you increase the value for this parameter. For instance, when you run `poetry run iterator --forloop --minimum 2 --maximum 10` it should produce the following output.

```
Calculating the powers of 2 from 2 to 10 with iteration:

  Should I use a for loop? Yes
  Should I use a while loop? No

  Here is the output with the for loop.

   2**2 = 4
   2**3 = 8
   2**4 = 16
   2**5 = 32
   2**6 = 64
   2**7 = 128
   2**8 = 256
   2**9 = 512

Wow, all of that iteration was exhausting! 😂
```

Note that this output shows that the first exponentiation that the `iterator` performs is `2**2 = 4` instead of starting with `2**0 = 1` as was the case in the previous runs.

```
Remember, if you want to run `iterator` you must use your terminal to go into the GitHub repository containing this project and then go into the `iterator` directory that contains the project's source code. Finally, remember that before running the program you must run `poetry install` to add the dependencies. If you run into errors when using a `poetry run` command you can often resolve them by deleting the `.venv` directry and the `poetry.lock` file and then trying `poetry install` again.
```

## Adding Functionality

If you study the file `iterator/iterator/main.py` you will see that it has many `TODO` markers that designate the parts of the program that you need to implement before `iterator` will produce the correct output. If you run the program before adding all of the source code required by the `TODO` markers then `iterator` will neither produce the correct output or pass the test suite. Ultimately, you are invited to add the required functionality to the functions that have the following signatures.

- Functions in the `display` module:

  - `def convert_bool_to_answer(argument: bool)`
  - `def display_list(values: List, indent="")`

- Functions in the `iterate` module:

  - `def calculate_powers_of_two_for_loop(minimum: int, maximum: int)`
  - `def calculate_powers_of_two_while_loop(minimum: int, maximum: int)`

It is important to note that you should not change the signature of these functions in your own implementation unless you receive prior approval from the course instructor.

When you are finished implementing both of the iterative approaches, please take time to evaluate each of them, comparing and contrasting their syntactic structure. Which one do you think is easier to understand? Why? Can you develop any good rules of thumb that suggest when it is better to use one type of loop over the other loop type?

Finally, the following source code segment shows how the `main` module should implement the Python source code that calls the `calculate_powers_of_two_for_loop` and `calculate_powers_of_two_while_loop` functions. Lines `1` and `7` of this source code segment ensure that the correct function in the `iterate` module is called. Next, lines `2` and `3` and `8` and `9` produce the correct labels that will appear in the console output. Finally, lines `4` and `10` call the correct iteration function depending on the command-line arguments specified by the person running the program. Once either the `calculate_powers_of_two_for_loop` or `calculate_powers_of_two_while_loop` function returns a list of values, the `display` function will show the contents of that list with the amount of indentation specified in the string constant.

```python
if forloop is True:
    typer.echo("  Here is the output with the for loop.")
    typer.echo("")
    forloop_list = iterate.calculate_powers_of_two_for_loop(minimum, maximum)
    display.display_list(forloop_list, "   ")
    typer.echo("")
if whileloop is True:
    typer.echo("  Here is the output with the while loop.")
    typer.echo("")
    whileloop_list = iterate.calculate_powers_of_two_while_loop(minimum, maximum)
    display.display_list(whileloop_list, "   ")
    typer.echo("")
````

## Project Reflection

Once you have finished both of the previous technical tasks, you can use a text editor to answer all of the questions in the `writing/reflection.md` file. For instance, you should provide the output of the Python program in a fenced code block, explain the meaning of the Python source code segments that you implemented and used, and answer all of the other questions about your experiences in completing this project.

## Submission

As you are working on your lab, you are to commit and push regularly. The commands are the following.

```bash
git add -A
git commit -m ``Your notes about commit here''
git push
```

After you have pushed your work to your repository, please visit the repository at the GitHub website (you may have to log-in using your browser) to verify that your files were correctly sent.

## Project Assessment

The grade that a student receives on this assignment will have the following components.

- **GitHub Actions CI Build Status [up to 50%]:**: For the lab01 repository associated with this assignment students will receive a checkmark grade if their last before-the-deadline build passes. This is only checking some baseline writing and commit requirements as well as correct running of the program. An additional reduction will given if the commit log shows a cluster of commits at the end clearly used just to pass this requirement. An addition reduction will also be given if there is no commit during lab work times. All other requirements are evaluated manually.

- **Mastery of Technical Writing [up to 25%]:**: Students will also receive a checkmark grade when the responses to the writing questions presented in the `reflection.md` reveal a proficiency of both writing skills and technical knowledge. To receive a checkmark grade, the submitted writing should have correct spelling, grammar, and punctuation in addition to following the rules of Markdown and providing conceptually and technically accurate answers.

- **Mastery of Technical Knowledge and Skills [up to 25%]**: Students will receive a portion of their assignment grade when their program implementation reveals that they have mastered all of the technical knowledge and skills developed during the completion of this assignment. As a part of this grade, the instructor will assess aspects of the programming including, but not limited to, the completeness and the correctness of the program and the use of effective source code comments.

---

## GatorGrade

### Checks for GatorGrade

For immediate feedback on submissions, we will be using Gator Grade to inform the of missing components in the submission. As you submit, you will notice that there is a thick red X that will change to a green check mark when all components have been included in the submission. You are encouraged to click on the red X to find a listing of the components to address.

You can check the baseline writing and commit requirements for this lab assignment by running department's assignment checking `gatorgrade` tool. To use `gatorgrade`, you first need to make sure you have Python3 installed (type `python --version` to check). If you do not have Python installed, please see:

- [Setting Up Python on Windows](https://realpython.com/lessons/python-windows-setup/)
- [Python 3 Installation and Setup Guide](https://realpython.com/installing-python/)
- [How to Install Python 3 and Set Up a Local Programming Environment on Windows 10](https://www.digitalocean.com/community/tutorials/how-to-install-python-3-and-set-up-a-local-programming-environment-on-windows-10)

Then, if you have not done so already, you need to install `gatorgrade`:

- First, [install `pipx`](https://pypa.github.io/pipx/installation/)
- Then, install `gatorgrade` with `pipx install gatorgrade`

Finally, you can run `gatorgrade`: `gatorgrade --config config/gatorgrade.yml`

## Seeking Assistance

* Extra resources for using markdown include;
  + [Markdown Tidbits](https://www.youtube.com/watch?v=cdJEUAy5IyA)
  + [Markdown Cheatsheet](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet)
* Do not forget to use the above git commands to push your work to the cloud for the instructor to grade your assignment. You can go to your GitHub repository using your browser to verify that your files have been submitted. Please see the TL’s or the instructor if you have any questions about assignment submission.

Students who have questions about this project outside of the lab time are invited to ask them in the course's Discord channel or during instructor's or TL's office hours.
