The goal of the primer is to enable you to perform a basic comparison of
two molecular structures with `aRMSD`, including proper installation of
the program. Here and there, the primer merely will *hint* you to
additional features implemented in `aRMSD`.

# setup of aRMSD

The project was reorganized around a `pyproject.toml` file, after
creation and activation of a virtual environment for Python 3.10 (or
higher), the command

``` bash
pip install .
```

on a copy of the GitHub project resolves the requirements from pypi.org.
Reserve about 0.8GB of permanent memory for this support. When
successful, the installation provides `armsd` as a new command to the
CLI.

## workflow

Except for widgets to provide an interactive structure display or user
adjustable diagrams about the test's statistics provided by matplotlib,
aRMSD lives in the command line. The following tree diagram recapituates
key points of the workflow on .xyz data.

``` markdown
├── reading input structures, for instance M1.xyz and M2.xyz
│
│
├── Consistency Checks and Structural Modification
│   ├── 0 to remove and exclude all hydrogens from the analysis
│   ├── 1 to remove all hydrogens bound to carbon
│   └── 3 to include all hydrogens in the analysis
│
│
├── Symmetry Adjustment & Sequency Matching
│   ├── visual inspection, any number or sequence of
│   │   ├── s to ave a .png (optional)
│   │   ├── left mouse button (LMB) to drag the scene
│   │   ├── Ctrl + LMB to roll the scene
│   │   ├── Shift + LMB to pan the scene
│   │   ├── mouse reel to zoom the scene
│   │   ├── r to return scene to a home position
│   │   ├── 3 toggle on/off stereoscopic anaglyph representation
│   │   └── q to quit and close the current widget
│   │
│   ├── any number or sequence of symmetry operations
│   │   ├── 1 for an inversoin at the origin
│   │   ├── 2 for a reflection on the xy plane
│   │   ├── 3 for a reflection on the xz plane
│   │   ├── 4 for a reflection on the yz plane
│   │   ├── 5 for a rotation around the x axis
│   │   ├── 6 for a rotation around the y axis
│   │   ├── 7 for a rotation around the z axis
│   │   └── 8 do not edit the relative orientation, show the molecules again
│   │
│   └── decide on the current alignment
│       └── 10 to save the current alignment for the next step
│
│
├──  decide over the program'ś matching algorithm used
│    ├── -1 continue with the current choice, or
│    ├── -2 change ge matching algorithm or solver
│    │   ├── -10 to leave the for the next upper level of hierarchy
│    │   ├── -1 to show detail;s of the currently used algorithm
│    │   ├── 1 use absolute distance between the atoms
│    │   ├── 2 use a combination of absolute and relative distances
│    │   ├── 3 use random permutations / brute force
│    │   ├── 4 use 'Hungarian' solver for the permutation matrix
│    │   └── 5 use 'aRMSD' solver for the permutation matrix (standard)
│    │
│    └── decide on the current atom match
│        ├── visual inspection (see above)
│        └── decide on the current state
│            ├── 0 to continue, because it is reasonably well aligned, or
│            └── return to manual adjustment of the initial alignment
│
│
└── Kabsch Algorithm, Statistics & Visualization
    ├── -1 Perform the Kabsch alignment (default), or
    ├── -2 Change the weighting function with either
    │   ├── 0 for geometric / unweighted (default)
    │   ├── 1 for x-ray scattering factors (Mo K\alpha)
    │   ├── 2 atomic masses
    │   ├── 3 total number of electrons
    │   ├── 4 number of core electrons
    │   ├── 5 spherical electron densities
    │   ├── 6 LDA electron densities
    │   └  -10 to return to the upper menu (then needs new a -1 for the test)
    │
    └── collect the results
        ├── 0 to visualize the results in a aRMSD representation
        ├── 1 visualize structural superposition
        ├── 2 perform statistics investigation of bond lengths and angles (plots)
        ├── 3 show RMSD results
        ├── 4 intrerpolate between the structures (cart., 10 steps)
        ├── 5 generate the permanent aRMSD_out.log file
        └── 20 export structure data, in either number or sequence of
            ├── 0 export superposition in two '.xyz' files
            ├── 1 export superposition in one '.xyzs' file
            ├── 2 export aRMSD representation in one '.xyzs' file
            └── -10 to return to the upper menu
```

For the analysis of `M1.xyz` and `M2.xyz` provided as test data in
folder `examples`, the optional log file written by `aRSMD` is provided
below:

``` shell
+------------------------------------------------------------------------------+
|              aRMSD - automatic RMSD Calculator (version 1.0.0)               |
|                      Arne Wagner, Norwid Behrnd (2026)                       |
|                                                                              |
|    A brief description of the program can be found in the manual and in:     |
|            A. Wagner, PhD thesis, University of Heidelberg, 2015.            |
|                                                                              |
|    Cite this program by:                                                     |
|    A. Wagner, H.-J. Himmel, J. Chem. Inf. Model, 2017, 57, 428-438           |
|    (doi: 10.1021/acs.jcim.6b00516),                                          |
|    source (http://www.github.com/nbehrnd/armsd), and version used.           |
+------------------------------------------------------------------------------+

                                                                     14-Jul-2026


*** Log file about the superposition of structures ***

    "Model"...                                                            M1.xyz
    "Reference"...                                                        M2.xyz

* Consistency establishment between the structures:

  The basic approach is to subsequently remove hydrogen atoms
  until the same number of atoms is found in both molecules.
  If the number of atoms is identical and the atom types belong
  to the same group in the periodic table, the molecules are
  considered as consistent.

    No disorder in the structures was found.

    Initial number of atoms in "Model"...                   	20  (7 H atoms)
    Initial number of atoms in "Reference"...               	20  (7 H atoms)

    Consistency between the structures was established:
    The number of atoms in "Model"...                       	20  (7 H atoms)
    The number of atoms in "Reference"...                   	20  (7 H atoms)

    No further modifications were performed.

    Final global atom count (number of hydrogens retained)...	20  (7 H atoms)

* Transformation of the molecules into "Standard Orientation":
  1. The center of mass was shifted to the Cartesian origin.
  2. The moment of inertia tensor was constructed, diagonalized
     and the eigenvectors rotated on the x, y and z axes.

* Details of the matching process:
    Structures were matched...                              	True
    Applied matching algorithm...                           	distance
    Solver used for matching...                             	hungarian
    Solution of the matching problem...                     	regular
    Number of highest deviations to be shown...             	5

    The highest deviations were between the pairs...           [Angstrom]
                                H-3 -- H-3                       0.51015
                                H-5 -- H-5                       0.53917
                                H-6 -- H-6                       0.57063
                               O-20 -- O-20                      0.59831
                               O-17 -- O-17                      0.72209
    The RMSD after the initial matching was [Angstrom]..    	0.21395

* Kabsch alignment:
    # General settings
    Substructures were defined...                           	False
    Weighting function for Kabsch algorithm...              	none
    Consideration of multi-center-contributions...          	False

    # Differentiation criteria and color information
    Number of colors for aRMSD plot...                      	19
    Maximum RMSD value for color projection [Angstrom]..    	0.7
    Threshold for bond comparison [Angstrom]...             	0.02
    Number of distance pairs above threshold...             	13
    Percentage of the colored intersections...              	9.999999999999998
    Color for shorter bonds in "Model" vs. "Reference"...   	#006400  [HEX]
    Color for longer bonds in "Model" vs. "Reference"...    	#CD0000  [HEX]
    Number of bonds below threshold...                      	13
    Color of "Model"...                                     	#CD0000  [HEX]
    Color of "Reference"...                                 	#006400  [HEX]

    Final rotation matrix from 'Standard Orientation':

           |-0.99992015  -0.01135453  -0.00554716|
     U  =  |+0.01155612  -0.99921955  -0.03777234|
           |-0.00511394  -0.03783343  +0.99927097|

    # This matrix aligns Model with Reference.
    # U already includes all custom symmetry operations!



* Final Quality of the Superposition:

    RMSD (Kabsch test, refined superposition [Angstrom])... 	0.20274
    Superposition R^2 (dimensionless)...                    	0.99499
    Cosine similarity (dimensionless)...                    	0.99827
    d values for the GARD calculation...                    	0.3, 1.2
    GARD score (dimensionless)...                           	0.80828

    For an introduction into the GARD calculation, see J. C. Baber,
    D. C. Thompson, J. B. Cross and C. Humblet, J. Chem. Inf. Model.,
    2009, 49, 1889-1900, doi: 10.1021/ci9001074.


* Decomposition into different atom types          absolute     relative
                                                  [Angstrom]      [%]
                              C    (#  9)          0.11504      (08.48)
                              H    (#  7)          0.20942      (28.10)
                              O    (#  4)          0.31464      (63.42)

    z-matrix properties:
    # z-matrices are created for both molecules, based on
    # (3 N - 1) bond distances, (3 N - 2) bond angles and
    # (3 N - 3) dihedral angles.  Both the total RMSD and
    # the relative contributions are calculated.
    RMSD [Angstrom]...                                      	0.38087
    Contribution of distances...                            	22.96  [%]
    Contribution of angles...                               	43.52  [%]
    Contribution of dihedral angles...                      	33.52  [%]

* Evaluation of structural parameters:
    # 1. The RMSE values are the root-mean-square errors
    #    between the corresponding properties of the two structures.
    # 2. The R**2 values are the the correlation coefficients
    #    between the two data sets.

    Number of bonds...                                      	20
    R**2 of linear correlation (dimensionless)...           	0.95576
    RMSE [Angstrom]...                                      	0.05050

    Number of bond types...                                 	3
    R**2 of linear correlation (dimensionless)...           	0.95576
    RMSE [Angstrom]...                                      	0.03130

    Number of angles...                                     	62
    R**2 of linear correlation (dimensionless)...           	0.75591
    RMSE [degrees]...                                       	2.84310

    Number of dihedrals...                                  	148
    R**2 of linear correlation (dimensionless)...           	0.99617
    RMSE [degrees]...                                       	4.26160


*** End of log file ***
```

The complete log of a test run with `M1.xyz` and `M2.xyz` as test data,
the report back to the BASH shell is provided below. Host system was an
instance of Linux Debian 13/trixie, supported by Python 3.13.5

``` shell

================================================================================
                          aRMSD (version 1.0.0, 2026)
================================================================================
               A. Wagner, University of Heidelberg (2015, 2017),
                           forked by N. Behrnd (2018)

--------------------------------- Description ----------------------------------
Key features:
* Parses data from various file formats
* Establishes consistency and matches coordinate sequences of two molecules
* Aligns two molecular structures based on the Kabsch algorithm
* Supports different weighting functions for the superposition
* Supports error propagation for experimental structures
* Generates different visualization types of the superposition results
* Writes outfiles that can be passed to other programs
* The original version was created by A. Wagner under Windows.  You find it
      hosted on GitHub: https://github.com/armsd/aRMSD.
* You are using a derivative fork based on the former, developed under Linux
      by N. Behrnd, hosted on GitHub: https://github.com/nbehrnd/aRMSD.

*** Cite this program as:
    A. Wagner, H.-J. Himmel, J. Chem. Inf. Model, 2017, 57, 428-438
    (doi: 10.1021/acs.jcim.6b00516); with address and version of aRMSD used.

Release dates of the individual modules:
- core module:    	'2026-07-14'
- plot module:    	'2026-07-03'
- log  module:    	'2026-07-14'

Module check:
- numpy         	'2.5.1'
- VTK           	'9.6.2'
- matplotlib    	'3.11.0'
- uncertainties 	'3.2.3'
- openbabel     	'3.2.1'
--------------------------------------------------------------------------------

Enter the file name with extension for the first file (comp./model)
>> M1.xyz

> 'M1.xyz' has been loaded successfully! (#Atoms: 20)

Enter the file name with extension for the second file (exp./reference)
>> M2.xyz

> 'M2.xyz' has been loaded successfully! (#Atoms: 20)
--------------------------------------------------------------------------------
... Files have been loaded!

--------------------------------------------------------------------------------
> Checking for coordinate standard deviations...
... No standard deviations were found!
--------------------------------------------------------------------------------

  Checking length unit of xyz coordinates ...
  The coordinate unit is [Angstrom]

  Checking length unit of xyz coordinates ...
  The coordinate unit is [Angstrom]

> The current status was saved successfully!


--------------------------------------------------------------------------------
================ Consistency Checks and Structural Modification ================
--------------------------------------------------------------------------------

> Performing consistency checks ... (Number of atoms: 20, 20)
  There are (7 & 7) H atoms in the molecules

> The structures of both molecules are consistent.

--------------------------------------------------------------------------------
    What should happen to the remaining 7 H-atoms?
--------------------------------------------------------------------------------
    Info: The exclusion of H-atoms in RMSD calculations is recommended if
          they were not located and refined in the X-ray experiment
--------------------------------------------------------------------------------
0   ... remove all hydrogen atoms (7)
3   ... keep all hydrogen atoms
--------------------------------------------------------------------------------

>>  Enter your choice: 3

> The molecules were rotated into 'Standard Orientation' ...

> The current status was saved successfully!

--------------------------------------------------------------------------------
=================== Symmetry Adjustments & Sequence Matching ===================
--------------------------------------------------------------------------------
-6  Set number of deviations which are highlighted in the plot (current = 5)
-5  Load the saved status (save point available: 'True')
-4  Change plot settings
-3  Manually swap atoms in Model structure
-2  Change matching algorithm or solver
-1  Match molecular sequences based on current alignment
--------------------------------------------------------------------------------
    Current matching algorithm  : 'distance'
    Current matching solver     : 'hungarian'
    Structures were matched     : 'False'
--------------------------------------------------------------------------------
0   ... exit the menu (no return)
1   ... inversion at the origin
2   ... reflection at the xy plane
3   ... reflection at the xz plane
4   ... reflection at the yz plane
5   ... rotation around the x axis
6   ... rotation around the y axis
7   ... rotation around the z axis
8   ... show the molecules again
--------------------------------------------------------------------------------
10  ... save current changes (status was saved: 'True')
20  ... export structures
--------------------------------------------------------------------------------

> Results are now shown in a separate window.
... To continue, quit the pop-up window with 'q'.
> To save the scene as *.png, press 's'.

>>  Enter your choice: 3

> Reflection of 'Model' structure at the xz-plane ...

--------------------------------------------------------------------------------
=================== Symmetry Adjustments & Sequence Matching ===================
--------------------------------------------------------------------------------
-6  Set number of deviations which are highlighted in the plot (current = 5)
-5  Load the saved status (save point available: 'True')
-4  Change plot settings
-3  Manually swap atoms in Model structure
-2  Change matching algorithm or solver
-1  Match molecular sequences based on current alignment
--------------------------------------------------------------------------------
    Current matching algorithm  : 'distance'
    Current matching solver     : 'hungarian'
    Structures were matched     : 'False'
--------------------------------------------------------------------------------
0   ... exit the menu (no return)
1   ... inversion at the origin
2   ... reflection at the xy plane
3   ... reflection at the xz plane
4   ... reflection at the yz plane
5   ... rotation around the x axis
6   ... rotation around the y axis
7   ... rotation around the z axis
8   ... show the molecules again
--------------------------------------------------------------------------------
10  ... save current changes (status was saved: 'True')
20  ... export structures
--------------------------------------------------------------------------------

> Results are now shown in a separate window.
... To continue, quit the pop-up window with 'q'.
> To save the scene as *.png, press 's'.

>>  Enter your choice: 4

> Reflection of 'Model' structure at the yz-plane ...

--------------------------------------------------------------------------------
=================== Symmetry Adjustments & Sequence Matching ===================
--------------------------------------------------------------------------------
-6  Set number of deviations which are highlighted in the plot (current = 5)
-5  Load the saved status (save point available: 'True')
-4  Change plot settings
-3  Manually swap atoms in Model structure
-2  Change matching algorithm or solver
-1  Match molecular sequences based on current alignment
--------------------------------------------------------------------------------
    Current matching algorithm  : 'distance'
    Current matching solver     : 'hungarian'
    Structures were matched     : 'False'
--------------------------------------------------------------------------------
0   ... exit the menu (no return)
1   ... inversion at the origin
2   ... reflection at the xy plane
3   ... reflection at the xz plane
4   ... reflection at the yz plane
5   ... rotation around the x axis
6   ... rotation around the y axis
7   ... rotation around the z axis
8   ... show the molecules again
--------------------------------------------------------------------------------
10  ... save current changes (status was saved: 'True')
20  ... export structures
--------------------------------------------------------------------------------

> Results are now shown in a separate window.
... To continue, quit the pop-up window with 'q'.
> To save the scene as *.png, press 's'.

>>  Enter your choice: 10

> The current status was saved successfully!

--------------------------------------------------------------------------------
=================== Symmetry Adjustments & Sequence Matching ===================
--------------------------------------------------------------------------------
-6  Set number of deviations which are highlighted in the plot (current = 5)
-5  Load the saved status (save point available: 'True')
-4  Change plot settings
-3  Manually swap atoms in Model structure
-2  Change matching algorithm or solver
-1  Match molecular sequences based on current alignment
--------------------------------------------------------------------------------
    Current matching algorithm  : 'distance'
    Current matching solver     : 'hungarian'
    Structures were matched     : 'False'
--------------------------------------------------------------------------------
0   ... exit the menu (no return)
1   ... inversion at the origin
2   ... reflection at the xy plane
3   ... reflection at the xz plane
4   ... reflection at the yz plane
5   ... rotation around the x axis
6   ... rotation around the y axis
7   ... rotation around the z axis
8   ... show the molecules again
--------------------------------------------------------------------------------
10  ... save current changes (status was saved: 'True')
20  ... export structures
--------------------------------------------------------------------------------

>>  Enter your choice: -1

--------------------------------------------------------------------------------

	The geometric RMSD of the current alignment is:  0.214 A

		 The 5 most disordered atom pairs are:
		Entry		      Pair		  Distance / A
		  5		   H-3 -- H-3   	    0.510
		  4		   H-5 -- H-5   	    0.539
		  3		   H-6 -- H-6   	    0.571
		  2		  O-20 -- O-20  	    0.598
		  1		  O-17 -- O-17  	    0.722

--------------------------------------------------------------------------------
=================== Symmetry Adjustments & Sequence Matching ===================
--------------------------------------------------------------------------------
-6  Set number of deviations which are highlighted in the plot (current = 5)
-5  Load the saved status (save point available: 'True')
-4  Change plot settings
-3  Manually swap atoms in Model structure
-2  Change matching algorithm or solver
-1  Match molecular sequences based on current alignment
--------------------------------------------------------------------------------
    Current matching algorithm  : 'distance'
    Current matching solver     : 'hungarian'
    Structures were matched     : 'True'
--------------------------------------------------------------------------------
0   ... exit the menu (no return)
1   ... inversion at the origin
2   ... reflection at the xy plane
3   ... reflection at the xz plane
4   ... reflection at the yz plane
5   ... rotation around the x axis
6   ... rotation around the y axis
7   ... rotation around the z axis
8   ... show the molecules again
--------------------------------------------------------------------------------
10  ... save current changes (status was saved: 'True')
20  ... export structures
--------------------------------------------------------------------------------

> Results are now shown in a separate window.
... To continue, quit the pop-up window with 'q'.
> To save the scene as *.png, press 's'.

>>  Enter your choice: 10

> The current status was saved successfully!

--------------------------------------------------------------------------------
=================== Symmetry Adjustments & Sequence Matching ===================
--------------------------------------------------------------------------------
-6  Set number of deviations which are highlighted in the plot (current = 5)
-5  Load the saved status (save point available: 'True')
-4  Change plot settings
-3  Manually swap atoms in Model structure
-2  Change matching algorithm or solver
-1  Match molecular sequences based on current alignment
--------------------------------------------------------------------------------
    Current matching algorithm  : 'distance'
    Current matching solver     : 'hungarian'
    Structures were matched     : 'True'
--------------------------------------------------------------------------------
0   ... exit the menu (no return)
1   ... inversion at the origin
2   ... reflection at the xy plane
3   ... reflection at the xz plane
4   ... reflection at the yz plane
5   ... rotation around the x axis
6   ... rotation around the y axis
7   ... rotation around the z axis
8   ... show the molecules again
--------------------------------------------------------------------------------
10  ... save current changes (status was saved: 'True')
20  ... export structures
--------------------------------------------------------------------------------

>>  Enter your choice: 0

> Exiting symmetry transformation menu ...

--------------------------------------------------------------------------------
================= Kabsch Algorithm, Statistics & Visualization =================
--------------------------------------------------------------------------------
-10 Exit aRMSD
-8  Plot aRMSD color map
-7  Change general RMSD settings
-6  Add/remove bond
-4  Change plot settings
-3  Define two substructures (structures are defined: 'False')
-2  Change weighting function
-1  Perform Kabsch alignment (required for all functions)
--------------------------------------------------------------------------------
    Current weighting function  : 'none'
    Calculate mcc contribution  : 'False'
    Kabsch alignment performed  : 'False'
--------------------------------------------------------------------------------
0   ... visualize results in aRMSD representation
1   ... visualize structural superposition
2   ... perform statistic investigation of bond lengths and angles
3   ... show RMSD results
4   ... interpolate between the structures (cart., 10 steps)
5   ... generate outfile
20  ... export structural data
--------------------------------------------------------------------------------

>>  Enter your choice: -1

--------------------------------------------------------------------------------
========================= Quality of the Superposition =========================
--------------------------------------------------------------------------------

> The type of weighting function is: 'none'


---------------------------- Similarity Descriptors ----------------------------
   >>>   Superposition R^2 :  0.99499
   >>>   Cosine similarity :  0.99827
   >>>   GARD score        :  0.80828


-------------------------- Root-Mean-Square-Deviation --------------------------
   >>>   RMSD              :  0.20274 Angstrom

   >>>   - Decomposition   :  Individual atom types  (total percentage)
           C    (#  9)     :  0.11504 Angstrom  (08.48 %)
           H    (#  7)     :  0.20942 Angstrom  (28.10 %)
           O    (#  4)     :  0.31464 Angstrom  (63.42 %)


----------------------------- Z-matrix properties ------------------------------
   >>>   RMSD              :  0.38087

   >>>   - Decomposition   :  total percentage
             distances     :  22.96 %
             angles        :  43.52 %
             dihedrals     :  33.52 %

--------------------------------------------------------------------------------
================= Kabsch Algorithm, Statistics & Visualization =================
--------------------------------------------------------------------------------
-10 Exit aRMSD
-8  Plot aRMSD color map
-7  Change general RMSD settings
-6  Add/remove bond
-4  Change plot settings
-3  Define two substructures (structures are defined: 'False')
-2  Change weighting function
-1  Perform Kabsch alignment (required for all functions)
--------------------------------------------------------------------------------
    Current weighting function  : 'none'
    Calculate mcc contribution  : 'False'
    Kabsch alignment performed  : 'True'
--------------------------------------------------------------------------------
0   ... visualize results in aRMSD representation
1   ... visualize structural superposition
2   ... perform statistic investigation of bond lengths and angles
3   ... show RMSD results
4   ... interpolate between the structures (cart., 10 steps)
5   ... generate outfile
20  ... export structural data
--------------------------------------------------------------------------------

>>  Enter your choice: 0

> Results are now shown in a separate window.
... To continue, quit the pop-up window with 'q'.
> To save the scene as *.png, press 's'.

--------------------------------------------------------------------------------
================= Kabsch Algorithm, Statistics & Visualization =================
--------------------------------------------------------------------------------
-10 Exit aRMSD
-8  Plot aRMSD color map
-7  Change general RMSD settings
-6  Add/remove bond
-4  Change plot settings
-3  Define two substructures (structures are defined: 'False')
-2  Change weighting function
-1  Perform Kabsch alignment (required for all functions)
--------------------------------------------------------------------------------
    Current weighting function  : 'none'
    Calculate mcc contribution  : 'False'
    Kabsch alignment performed  : 'True'
--------------------------------------------------------------------------------
0   ... visualize results in aRMSD representation
1   ... visualize structural superposition
2   ... perform statistic investigation of bond lengths and angles
3   ... show RMSD results
4   ... interpolate between the structures (cart., 10 steps)
5   ... generate outfile
20  ... export structural data
--------------------------------------------------------------------------------

>>  Enter your choice: 1

> Results are now shown in a separate window.
... To continue, quit the pop-up window with 'q'.
> To save the scene as *.png, press 's'.

--------------------------------------------------------------------------------
================= Kabsch Algorithm, Statistics & Visualization =================
--------------------------------------------------------------------------------
-10 Exit aRMSD
-8  Plot aRMSD color map
-7  Change general RMSD settings
-6  Add/remove bond
-4  Change plot settings
-3  Define two substructures (structures are defined: 'False')
-2  Change weighting function
-1  Perform Kabsch alignment (required for all functions)
--------------------------------------------------------------------------------
    Current weighting function  : 'none'
    Calculate mcc contribution  : 'False'
    Kabsch alignment performed  : 'True'
--------------------------------------------------------------------------------
0   ... visualize results in aRMSD representation
1   ... visualize structural superposition
2   ... perform statistic investigation of bond lengths and angles
3   ... show RMSD results
4   ... interpolate between the structures (cart., 10 steps)
5   ... generate outfile
20  ... export structural data
--------------------------------------------------------------------------------

>>  Enter your choice: 2

> Results are now shown in a separate window.
... To continue, quit the pop-up window with 'q'.


---------------- The Highest Deviations in Internal Coordinates ----------------
The 3 highest deviations are printed below
Entries are: Atoms, values in the Model and Reference, difference
--------------------------------------------------------------------------------
 >> Bonds (in Angstrom):
    1.  [C-15, C-16] 1.455 1.598	Diff. 0.14300000000000002
    2.  [C-8, O-17] 1.252 1.143	Diff. -0.10899999999999999
    3.  [C-8, C-9] 1.49 1.55	Diff. 0.06000000000000005
--------------------------------------------------------------------------------
 >> Bond angles (in deg.):
    1.  [O-17, C-8, O-18] 119.78 128.56	Diff. 8.780000000000001
    2.  [O-18, C-8, O-17] 119.78 128.56	Diff. 8.780000000000001
    3.  [O-18, C-8, C-9] 117.731 112.809	Diff. -4.921999999999997
--------------------------------------------------------------------------------
 >> Dihedral angles (in deg.):
    1.  [C-14, C-9, C-8, O-18] 35.01 50.081	Diff. 15.071000000000005
    2.  [O-18, C-8, C-9, C-14] 35.01 50.081	Diff. 15.071000000000005
    3.  [O-17, C-8, C-9, C-14] 144.42 130.267	Diff. -14.152999999999992
--------------------------------------------------------------------------------

--------------------------------------------------------------------------------
================= Kabsch Algorithm, Statistics & Visualization =================
--------------------------------------------------------------------------------
-10 Exit aRMSD
-8  Plot aRMSD color map
-7  Change general RMSD settings
-6  Add/remove bond
-4  Change plot settings
-3  Define two substructures (structures are defined: 'False')
-2  Change weighting function
-1  Perform Kabsch alignment (required for all functions)
--------------------------------------------------------------------------------
    Current weighting function  : 'none'
    Calculate mcc contribution  : 'False'
    Kabsch alignment performed  : 'True'
--------------------------------------------------------------------------------
0   ... visualize results in aRMSD representation
1   ... visualize structural superposition
2   ... perform statistic investigation of bond lengths and angles
3   ... show RMSD results
4   ... interpolate between the structures (cart., 10 steps)
5   ... generate outfile
20  ... export structural data
--------------------------------------------------------------------------------

>>  Enter your choice: 3

--------------------------------------------------------------------------------
========================= Quality of the Superposition =========================
--------------------------------------------------------------------------------

> The type of weighting function is: 'none'


---------------------------- Similarity Descriptors ----------------------------
   >>>   Superposition R^2 :  0.99499
   >>>   Cosine similarity :  0.99827
   >>>   GARD score        :  0.80828


-------------------------- Root-Mean-Square-Deviation --------------------------
   >>>   RMSD              :  0.20274 Angstrom

   >>>   - Decomposition   :  Individual atom types  (total percentage)
           C    (#  9)     :  0.11504 Angstrom  (08.48 %)
           H    (#  7)     :  0.20942 Angstrom  (28.10 %)
           O    (#  4)     :  0.31464 Angstrom  (63.42 %)


----------------------------- Z-matrix properties ------------------------------
   >>>   RMSD              :  0.38087

   >>>   - Decomposition   :  total percentage
             distances     :  22.96 %
             angles        :  43.52 %
             dihedrals     :  33.52 %

--------------------------------------------------------------------------------
================= Kabsch Algorithm, Statistics & Visualization =================
--------------------------------------------------------------------------------
-10 Exit aRMSD
-8  Plot aRMSD color map
-7  Change general RMSD settings
-6  Add/remove bond
-4  Change plot settings
-3  Define two substructures (structures are defined: 'False')
-2  Change weighting function
-1  Perform Kabsch alignment (required for all functions)
--------------------------------------------------------------------------------
    Current weighting function  : 'none'
    Calculate mcc contribution  : 'False'
    Kabsch alignment performed  : 'True'
--------------------------------------------------------------------------------
0   ... visualize results in aRMSD representation
1   ... visualize structural superposition
2   ... perform statistic investigation of bond lengths and angles
3   ... show RMSD results
4   ... interpolate between the structures (cart., 10 steps)
5   ... generate outfile
20  ... export structural data
--------------------------------------------------------------------------------

>>  Enter your choice: 5

> A logfile (aRMSD_logfile.out) has been written successfully!

--------------------------------------------------------------------------------
================= Kabsch Algorithm, Statistics & Visualization =================
--------------------------------------------------------------------------------
-10 Exit aRMSD
-8  Plot aRMSD color map
-7  Change general RMSD settings
-6  Add/remove bond
-4  Change plot settings
-3  Define two substructures (structures are defined: 'False')
-2  Change weighting function
-1  Perform Kabsch alignment (required for all functions)
--------------------------------------------------------------------------------
    Current weighting function  : 'none'
    Calculate mcc contribution  : 'False'
    Kabsch alignment performed  : 'True'
--------------------------------------------------------------------------------
0   ... visualize results in aRMSD representation
1   ... visualize structural superposition
2   ... perform statistic investigation of bond lengths and angles
3   ... show RMSD results
4   ... interpolate between the structures (cart., 10 steps)
5   ... generate outfile
20  ... export structural data
--------------------------------------------------------------------------------

>>  Enter your choice: -10

--------------------------------------------------------------------------------
========================== Normal program termination ==========================
--------------------------------------------------------------------------------



```
