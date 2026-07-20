# aRMSD

After the installation of `aRMSD`, this primer outlines the comparison
of two conformers of a small molecule. Briefly, functionality beyond
basic use is indicated, too.

# setup of aRMSD

It is recommended to install and use `aRMSD` within a virtual
environment of Python 3.11 (or above). Either download the .zip archive,
or clone the [GitHub repository](https://github.com/nbehrnd/aRMSD). By
the command of

``` bash
pip install .
```

within this folder, `pyproject.toml` resolves the program's dependencies
on [pypi.org](https://pypi.org/). Be aware this support requires up to
about 0.8GB of permanent memory. When successful, the installation
provides the CLI `armsd` (all lowercase) as a new command.

# workflow overview

The following tree diagram recapitulates key points of the workflow on
.xyz data. Files `M1.xyz` and `M2.xyz` can be found in folder
`examples`.

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

# reference outputs

## optional permanent record `aRMSD_logfile.out`

`aRMSD` allows to recapitulate the analysis in a permanent record, file
`aRMSD_logfile.out`. In the flow chart, this is option `5` of section
"collect the results". Below is the summary of the successful Kabsch
test with example data `M1.xyz` and `M2.xyz`:

``` text
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

## CLI log of a successful comparison

Except `vtk` widgets to visualize the structures, and diagrams by
`matplotlib`, the program lives in the CLI. Depending on your setup
used, it is possible that lines with program options are visually
truncated and in consequence, accidentally missed. It is for this reason
why the complete dialog on the CLI for a Kabsch test of structures files
`M1.xyz` and `M2.xyz` is provided below.

The two test data are provided by the GitHub repository (folder
`examples`), the Kabsch test was run in an instance of Linux
Debian 13/trixie with Python 3.13.5.

``` text

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

# Example geometric Kabsch test

This chapter describes a simple *geometric* Kabsch test of two
conformers of a small molecule. Here, the test is *geometric* because
the contribution of each atom to the final RMSD only depends on its
atomic position, and the incertitude of this atomic position. It is the
basic approach in `aRMSD` and suitable to get familiar with the program,
especially in conjunction with the *workflow overview* this primer
includes.

The test data used are files `M1.xyz` and `M2.xyz` (folder `examples`)
about the aspirinate anion. They are derived from corresponding `*.cif`
found in the CSD data base[^1] with Olex2.[^2] Copy these into a
location easily accessible for you.

Side note: Depending on the use case, it might be useful, or necessary
to equally account for atomic properties such as atomic masses, total or
core electron count, atomic X-ray scattering factors, etc. These options
contribute to a *weighted* Kabsch test and represent an advanced used of
`aRMSD` described in a different chapter.

## Reading the structures

From your shell, launch the program by command `aRMSD`.

After the simulated prompt (the `>` sign), enter the complete file name
(including the file extension) of the first model to load and confirm
with with `ENTER`. Note, there is no tab-assisted auto-completion of the
file name. If you err with the file name, and the model does not exist,
you are offered a new prompt. If you err with the file name pointing to
an existing model, but are not interested to compare with an other
model, the simplest rectification is to close `aRMSD` with `Ctrl + C`
and to start the program freshly again.

![](./docSources/aRMSD-loadingModels.png)

The program's note

``` bash
No standard deviations were found!
```

reminds the program's background in crystallography, where atomic
coordinates may be described with their esd. Present `aRMSD` (version
1.0.0) however is not yet (again) capable to reliably process `.cif`
files. With `.xyz` files – as in this example– you don't need to worry
about this note.

Side note: Indeed, it is possible to load different models of different
file type with different file extensions, such as `M1.xyz` for the
first, and `M2.pdb` for the second model to compare with each other.
While preparing the Kabsch test, as long as *consistency checks* on the
two model's total atom count are passed, this is not problematic to
`aRMSD`.

### Consideration of hydrogen atoms

For the Kabsch test ahead, `aRMSD` allows you to include all, or to
exclude a selection of hydrogens (bond to carbons, or bond to group-14
elements). You equally may neglect all hydrogen atoms altogether, too.
This can be useful e.g., for comparing two structure models where one
has an incomplete set of hydrogen atoms as obtained e.g., by X-ray
diffraction experiments.

Your choice here only affects the internal representation of model and
reference. Your choice will not edit your input files.

For the purpose of this primer, all atoms were included in the scrutiny,
selected by key stroke `3`:

![](./docSources/aRMSD-hydrogens.png)

`aRMSD` then provides a first *guess* of an *initial alignment* the two
models.

## User-assisted re-orientation of the models

`aRMSD` now launches a `vtk`-based widget separate from the terminal.
With your mouse, you can tilt, roll, pan, and zoom the scene to your
preference to learn about this *initial* alignment were the *model* (red
motif) and *reference* (green motif) already share a Cartesian
coordinate system in common. Depending on your computer and operating
system, it is possible to toggle on/off an anaglyph representation, too.

![](./docSources/aRMSD-structureVisualizerDefault-scaled.png)

| command                                 | function                  |
|-----------------------------------------|---------------------------|
| dragging with left mouse button (`LMB`) | tilt the scene            |
| `CTRL + LMB`                            | roll the scene            |
| `Shift + LMB`                           | pane the scene            |
| middle mouse reel                       | zoom the scene            |
| `r`                                     | return to a home position |
| `3`                                     | toggle anaglyph display   |
| `q`, `e`, or `0`                        | close the visualizer      |
| `s`                                     | save the scene (`*.png`)  |

Note that the more your mouse is out of the center of the visualizer's
canvas, the more the mouse-assisted actions accelerate. You may document
the match as bitmap with key-stroke `s`; the visualizer, unaltered in
its default dimension will write a `*.png` (2048 ×2048 px) deposit in
your current working directory.

If you are familiar about the alignment shown to you, close the
visualizer (`q`). If – as in the current example – the two model data do
not align nicely, the terminal offers you multiple symmetry operations
to try a better alignment. Each time you select one of the options,
`aRMSD` displays a new *initial match* of the two in a newly opened
instance of the visualizer.

![](./docSources/aRMSD-realignmentInterface.png)

In the case of this primer, the relative arrangement has to undergo an
inversion (key-stroke `1`), and an reflection in respect to the
*xz*-plane (key-stroke `3`). The approach is iterative, and the sequence
these operations does not matter. The progress is shown in the figure
below. Intentionally both alignments shown share the same perspective.

![](./docSources/aRMSD-M1M2-initialMatching.png)

At this stage, you aim for a fit of the two model structures that is
*good enough*. (In the ongoing of this section, as well in comparison
with the next chapter, you will learn what this refers to.) Once two
structure data do overlap – again, it is *an initial* superposition only
– close the visualizer (keystroke `q`) and save this change alignment
obtained (with keystroke `10`).

## Re-ordering of the atoms

To proceed in the refinement of the superposition successfully, the
atoms recognized of both models have to be labeled consistently. *One*
approach available in `aRMSD` is the Hungarian algorithm, implemented as
default strategy. At the current stage of the analysis, this is
triggered by hitting `-1` (minus one).

`aRMSD` will again open a `vtk`-visualizer of the two prealigned models.
In contrast to the former situation, however, the labeling of the atoms
of one molecule should match the one of the same atoms in the second
molecule. In addition, yellow streaks indicate which atoms in *model*
and *reference* `aRMSD` considers as equivalent.

![](./docSources/aRMSD-M1M2-Hungarian.png)

Since the obtained pre-alignment and match of atom sequences is
reasonable, close the visualizer (key-stroke `q`), and save the
intermediate result (key-stroke `10`).

## refinement of the superposition (Kabsch test)

To enter the menu about the Kabsch test, hit now once `0` (zero). The
interface displayed by `aRMSD` in the terminal changes, and you are able
to trigger the refinement of the superposition with `-1` (minus one).
The now following sequence of calling subroutines is *recommended* to
harvest the maximum of relevant data `aRMSD` provides.

![](./docSources/aRMSD-KabschInterface.png)

- Key-stroke `0` (zero) again opens the interactive Vtk-based visualizer
  (subfigure a). This adapted ball-stick representation displays *atom
  radii* of the atoms proportional to the *relative contribution* of
  said atoms to the global RMSD. The *atom colors* of the spheres scales
  to the absolute remaining difference of the two fit structures about
  said atom in Angstroms. The lateral scale offers an estimate of the
  latter.

![](./docSources/aRMSD-diffA-diffB.png)

Some of the bonds depicted *might* bear a red band in the center. This
is to indicate that the same bond in the reference model is
significantly shorter, than in the tested model. Conversely, a green
band indicates a bond that is longer. By default, the critical *length
difference* to set these bands equals to 0.2 Angstrom. Bby keystroke `1`
(subfigure b), a wireframe model of the finalized superposition.

Clicking *on* a representation of one, two, three, or four atoms selects
them to read out to the final RMSD data about the corresponding
position; or corresponding difference in distance, angle; or dihedral
angle between model and reference. These readouts are non-permanent and
provided *only* on the terminal.

![](./docSources/aRMSD-diffTest.png)

The underlying routine providing the readouts is agnostic about the atom
type, allowing both the selection of hydrogen atoms, as well as non-H
atoms. The atoms of interest need not be adjacent, either, which may be
of interest comparing distances and angles. Again, you close the
visualizer with keystroke `q`.

- With key-stroke `2`, an additional determination of statistics, and
  generation of synoptic diagrams is provided by the `matplotlb`
  library. At your discretion, you can pan and zoom to the region of
  interest within the diagrams. Depending on your setup, the diagrams
  can then be exported for instance as `.png`, `.pdf`, or `.tikz`.

![](./docSources/aRMSD-M1M2-statistics.png)

The window about the statistics plots may be closed either by mouse, or
again key-stroke `q`.

- With keystroke `3`, the program offers you a first decomposition about
  RMSD's contributions onto the terminal. Though your shell might
  visually truncate some of the results, it is useful to invoke this
  subroutine once – even blindly – because *this step's results* will
  enter the permanent record log written of the next.

![](./docSources/aRMSD-M1M2SuperposQuality.png)

- Key-stroke `5` initiates `aRMSD` to write a permanent record
  `aRMSD_log-file.out` as plain text. This recapitulates setup and
  results of the similarity measurement, such as the rotation matrix
  applied to match the two structure models, or further figures of merit
  (e.g., cosine similarity, GARD similarity).

  In section `reference outputs`, the primer includes an example of
  `aRMSD_logfile.out`.

## general hints

Last, but not least, a few words of caution:

- It is normal that performing the same computation a twice, with the
  same files, in a different operating system yields results *slightly
  different* from each other.

- There are multiple "dialects" about the `.pdb` format, which may
  require the model data you have to be converted into `.xyz`, for
  example with `babel`[^3] using a pattern of

  ``` shell
  babel input.pdb -O converted.xyz
  ```

  The conversion into `.xyz` may strip symmetry of the structure model,
  and thus affect file size.

# Example of a failed Kabsch test

This section compiles hints of various degrees to recognize the Kabsch
test *might be*, or actually *is* on the wrong track.

Let's presume the program's guess of a prealignment wasn't yet optimal,
and the manual adjustment by symmetry operations incomplete. Then,
running the Hungarian algorithm to synchronize the atom sequence in
*model* and *reference* may fail. Or, though successful in this task,
the subsequent representation highlights the corresponding atoms by
yellow struts running largely across the coordinate system in common.
The figure below displays such at level where atoms are labeled (a), and
corresponding atom is assigned (b).

![](./docSources/aRMSD-badAlignmentOnlyInversion-stepA.png)

While mathematically still possible to perform a Kabsch test, another
warning indicator are atoms depicted with unusual large absolute
contribution to the overall final RMSD (subfigure a). Depending on the
structure model and its molecular symmetry in question, some atoms might
be more affected by a misalignment, than others. Trying to connect the
atoms of either *model*, or *reference*, `aRMSD` might depict unusually
distorted structures (subfigure b), too

![](./docSources/aRMSD-badAlignmentOnlyInversion-stepB.png)

Eventually, the visual inspection (and comparison with other attempts)
of the statistic diagrams should complement the reading of the
corresponding optional `aRMSD_logfile.out`.

![](./docSources/aRMSD-badAlignmentOnlyInversion-stepC.png)

[^1]: Model `M1.xyz` and `M1.pdb` are derivated from entry `FEHGAB` of
    CCDC's CSD file; primary reference: Santana, M. D.; Lozano, A. A.;
    García, G.; López, G.; Pérez, J. Five-Coordinate Nickel(ii)
    Complexes with Carboxylate Anions and Derivatives of
    1,5,9-Triazacyclododec-1-Ene: Structural and1 H NMR Spectroscopic
    Studies. *Dalton Trans.* **2005**, No. 1, 104–109.
    <https://doi.org/10.1039/B413547D>. `M2.xyz` and `M2.pdb` are
    derivated from entry `IVUYEE` of CCDC's CSD file; primary reference:
    Poyraz, M.; Banti, C. N.; Kourkoumelis, N.; Dokorou, V.; Manos, M.
    J.; Simčič, M.; Golič-Grdadolnik, S.; Mavromoustakos, T.;
    Giannoulis, A. D.; Verginadis, I. I.; Charalabopoulos, K.;
    Hadjikakou, S. K. Synthesis, Structural Characterization and
    Biological Studies of Novel Mixed Ligand Ag(I) Complexes with
    Triphenylphosphine and Aspirin or Salicylic Acid. *Inorg. Chim.
    Acta* **2011**, *375* (1), 114–121.
    <https://doi.org/10.1016/j.ica.2011.04.032>.

[^2]: Dolomanov, O. V.; Bourhis, L. J.; Gildea, R. J.; Howard, J. A. K.;
    Puschmann, H. OLEX2 : A Complete Structure Solution, Refinement and
    Analysis Program. *J. Appl. Crystallogr.* **2009**, *42* (2),
    339–341. <https://doi.org/10.1107/S0021889808042726>. Olex2,
    version 1.2.10.

[^3]: Open Babel, <http://openbabel.org/>. For further details, see
    O’Boyle, N. M.; Banck, M.; James, C. A.; Morley, C.; Vandermeersch,
    T.; Hutchison, G. R. Open Babel: An Open Chemical Toolbox. *J
    Cheminform* **2011**, *3* (1), 33.
    <https://doi.org/10.1186/1758-2946-3-33>.
