This is a quick, hacky script that will turn an ASCII diagram like this one:

	-------------------------------------------------------------------------------------------------
	|31|30|29|28|27|26|25|24|23|22|21|20|19|18|17|16|15|14|13|12|11|10| 9| 8| 7| 6| 5| 4| 3| 2| 1| 0|
	-------------------------------------------------------------------------------------------------
	|Condition  |0 |0 |0 |Operation  |S |$R_n$      |$R_d$      |$S_\text{amt}$|$S_t$|0 |*1         |
	-           -  -  -  -           -  -           -           ----------------     ----           -
	|           |  |  |  |           |  |           |           |*2         |0 |     |1 |           |
	-           -  -  ----           -  -           -           -------------------------------------
	|           |  |  |1 |           |  |           |           |*3         |Immediate              |
	-------------------------------------------------------------------------------------------------
	

into the code for a latex table looking like it:

	\begin{tabular}{|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|}
	\hline
	31 & 30 & 29 & 28 & 27 & 26 & 25 & 24 & 23 & 22 & 21 & 20 & 19 & 18 & 17 & 16 & 15 & 14 & 13 & 12 & 11 & 10 & 9 & 8 & 7 & 6 & 5 & 4 & 3 & 2 & 1 & 0  \\
	\hline
	\multicolumn{4}{|c|}{\multirow{3}{*}{Condition}} & \multirow{3}{*}{0} & \multirow{3}{*}{0} & \multirow{2}{*}{0} & \multicolumn{4}{|c|}{\multirow{3}{*}{Operation}} & \multirow{3}{*}{S} & \multicolumn{4}{|c|}{\multirow{3}{*}{$R_n$}} & \multicolumn{4}{|c|}{\multirow{3}{*}{$R_d$}} & \multicolumn{5}{|c|}{$S_\text{amt}$} & \multicolumn{2}{|c|}{\multirow{2}{*}{$S_t$}} & 0 & \multicolumn{4}{|c|}{\multirow{2}{*}{*1}}  \\
	\cline{21-25}\cline{28-28}
	\multicolumn{4}{|c|}{} & & & & \multicolumn{4}{|c|}{} & & \multicolumn{4}{|c|}{} & \multicolumn{4}{|c|}{} & \multicolumn{4}{|c|}{*2} & 0 & \multicolumn{2}{|c|}{} & 1 & \multicolumn{4}{|c|}{}  \\
	\cline{7-7}\cline{21-32}
	\multicolumn{4}{|c|}{} & & & 1 & \multicolumn{4}{|c|}{} & & \multicolumn{4}{|c|}{} & \multicolumn{4}{|c|}{} & \multicolumn{4}{|c|}{*3} & \multicolumn{8}{|c|}{Immediate}  \\
	\hline
	\end{tabular}

![Example table](https://github.com/yuriks/ascii2latex/raw/master/diag1.png)

As you can see, it supports both column and row spanning.

It was done quite recklessly and will probably blow up on incorrectly formatted input. Notably, the input file requires an empty line at the end.
