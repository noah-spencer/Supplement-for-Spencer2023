add_library('pdf')
hint(ENABLE_STROKE_PURE)

### Set working directory.
workdir = ""

### Set colors of genes based on functional category. Pseudogene coloration (gray by default) will override category color.
Gene_list = ['rRNA','riboprot','biosynth','chaperone','tRNA','Other']
Gene_colors  = {'rRNA': [220,38,127], #magenta
                'riboprot': [90,67,195], #purple
                'biosynth': [254,97,0], #orange
                'chaperone': [255,176,0], #gold
                'tRNA': [0,0,0], #black
                'Other': [100,143,255]} #blue

### Set color to display the read coverage of each sample.
Spec_colors  = {'RNA_174B': [20,20,20], #transluscent gray
                'RNA_188B': [20,20,20],
                'RNA_193B': [20,20,20]}

### List of samples/specimens/sequencing libraries.
SPEC_LIST = ["RNA_174B", "RNA_188B", "RNA_193B"]
#SPEC_LIST = ["RNA_1163B", "RNA_1164B", "RNA_1183B"]
#SPEC_LIST = ["RNA_416B", "RNA_418B", "RNA_419B"]
#SPEC_LIST = ["RNA_1236B", "RNA_1238B", "RNA_1239B"]
#SPEC_LIST = ["RNA_416B", "RNA_418B", "RNA_419B"]
#SPEC_LIST = ["F17B", "F30B"]

### List of contigs -- each is plotted separately.
GENOME_LIST = ["DICSEM"]
#GENOME_LIST = ["TETULN"]
#GENOME_LIST = ["TETUND1", "TETUND2"]
#GENOME_LIST = ["OKAORE1", "OKAORE2", "OKAORE3", "OKAORE4"]
#GENOME_LIST = ["TETLIM1", "TETLIM2", "TETLIM3", "TETLIM4", "TETLIM5"]
#GENOME_LIST = ["CM008730.1", "CM008741.1", "CM008752.1", "CM008763.1", "CM008764.1", "CM008765.1", "CM008766.1", "CM008767.1", "CM008768.1", "CM008731.1", "CM008732.1", "CM008733.1", "CM008734.1", "CM008735.1", "CM008736.1", "CM008737.1", "CM008738.1", "CM008739.1", "CM008740.1", "CM008742.1", "CM008743.1", "CM008744.1", "CM008745.1", "CM008746.1", "CM008747.1", "CM008748.1", "CM008749.1", "CM008750.1", "CM008751.1", "CM008753.1", "CM008754.1", "CM008755.1", "CM008756.1", "CM008757.1", "CM008758.1", "CM008759.1", "CM008760.1", "CM008761.1", "CM008762.1", "NXGN01000045.1", "NXGN01000040.1", "NXGN01000041.1", "NXGN01000042.1", "NXGN01000043.1", "NXGN01000044.1", "NXGN01000046.1", "NXGN01000047.1", "NXGN01000048.1", "NXGN01000049.1", "NXGN01000050.1", "NXGN01000051.1", "NXGN01000052.1", "NXGN01000053.1", "NXGN01000054.1", "NXGN01000055.1", "NXGN01000056.1", "NXGN01000057.1", "NXGN01000058.1", "NXGN01000059.1", "NXGN01000060.1", "NXGN01000061.1", "NXGN01000062.1", "NXGN01000063.1", "NXGN01000064.1", "NXGN01000093.1", "NXGN01000066.1", "NXGN01000065.1", "NXGN01000068.1", "NXGN01000067.1", "NXGN01000069.1", "NXGN01000070.1", "NXGN01000072.1", "NXGN01000071.1", "NXGN01000073.1", "NXGN01000074.1", "NXGN01000075.1", "NXGN01000076.1", "NXGN01000077.1", "NXGN01000078.1", "NXGN01000079.1", "NXGN01000080.1", "NXGN01000081.1", "NXGN01000082.1", "NXGN01000083.1", "NXGN01000084.1", "NXGN01000085.1", "NXGN01000086.1", "NXGN01000087.1", "NXGN01000088.1", "NXGN01000089.1", "NXGN01000090.1", "NXGN01000091.1", "NXGN01000092.1", "NXGN01000104.1", "NXGN01000094.1", "NXGN01000095.1", "NXGN01000096.1", "NXGN01000097.1", "NXGN01000098.1", "NXGN01000099.1", "NXGN01000100.1", "NXGN01000101.1", "NXGN01000102.1", "NXGN01000103.1", "NXGN01000105.1", "NXGN01000106.1", "NXGN01000107.1", "NXGN01000108.1", "NXGN01000109.1", "NXGN01000110.1", "NXGN01000111.1", "NXGN01000112.1", "NXGN01000113.1", "NXGN01000114.1", "NXGN01000115.1", "NXGN01000116.1", "NXGN01000117.1", "NXGN01000118.1", "NXGN01000119.1", "NXGN01000120.1", "NXGN01000121.1", "NXGN01000122.1", "NXGN01000123.1", "NXGN01000124.1", "NXGN01000125.1", "NXGN01000126.1", "NXGN01000127.1", "NXGN01000128.1", "NXGN01000129.1", "NXGN01000130.1", "NXGN01000131.1", "NXGN01000132.1", "NXGN01000133.1", "NXGN01000134.1", "NXGN01000135.1", "NXGN01000136.1", "NXGN01000137.1", "NXGN01000138.1", "NXGN01000139.1", "NXGN01000140.1", "NXGN01000141.1", "NXGN01000142.1", "NXGN01000143.1", "NXGN01000144.1", "NXGN01000145.1", "NXGN01000146.1", "NXGN01000147.1", "NXGN01000148.1", "NXGN01000149.1", "NXGN01000150.1", "NXGN01000151.1", "NXGN01000152.1", "NXGN01000153.1", "NXGN01000154.1", "NXGN01000155.1", "NXGN01000156.1", "NXGN01000157.1", "NXGN01000158.1", "NXGN01000159.1", "NXGN01000160.1", "NXGN01000161.1", "NXGN01000162.1", "NXGN01000163.1"]

#GENOME_LIST = ["SMDICSEM"]
#GENOME_LIST = ["SMTETULN"]
#GENOME_LIST = ["SMTETUND"]
#GENOME_LIST = ["SMOKAORE"]
#GENOME_LIST = ["SMTETLIM"]
#GENOME_LIST = ["SMMAGSEP"]

def CalculateCoverage(coverage):
    if coverage == 0:
        COV = 0
    else:
        COV = coverage
    return(max(0,COV))

### Function for setting fill color, of contigs or legend
def SelectColor(gene_category, opacity):
    if gene_category in Gene_list:
        fill(Gene_colors[gene_category][0],Gene_colors[gene_category][1],Gene_colors[gene_category][2],opacity)
        stroke(Gene_colors[gene_category][0],Gene_colors[gene_category][1],Gene_colors[gene_category][2],opacity)
        return("")

def SelectColorSample(sample, opacity):
    fill(Spec_colors[sample][0],Spec_colors[sample][1],Spec_colors[sample][2],opacity)
    stroke(Spec_colors[sample][0],Spec_colors[sample][1],Spec_colors[sample][2],opacity)
    return("")


size(2600, 1400)

for genome in GENOME_LIST:
    print("Processing genome %s" % genome)
    textSize(60)
    textAlign(LEFT)
    text(genome,50,60)

    REFERENCE = loadTable(workdir + genome + ".pro", "csv")

    Output_name = genome + ".pdf"
    beginRecord(PDF, Output_name)


    background(255)
    scale_x = x_scale = 70
    scale_y = 5
    scale_tick = 5000
    start_x = 150
    start_y = 700

    row = REFERENCE.getRow(0)
    Ref_size = row.getInt(2)

    ### Draw REFERENCE genes
    for i in range(1, REFERENCE.getRowCount()):
        Entry = REFERENCE.getRow(i)
        Gene = Entry.getString(1)
        Gene_category = Entry.getString(2)
        Gene_functionality = Entry.getString(3)
        Gene_start = Entry.getInt(4)
        Gene_end = Entry.getInt(5)
        Gene_orientation = Entry.getString(6)

        print(Gene, Gene_category, Gene_start, Gene_end, Gene_orientation)
        stroke(0,0,0,0)
        strokeWeight(0)

        """
        if Gene_category != "Other":
            SelectColor(Gene_category,30)
            strokeWeight(0)
            rect(start_x+Gene_start/scale_x, start_y, (Gene_end-Gene_start)/scale_x, -(start_y-baseline_y))
        """
        if Gene_category == "Pseudo":
            fill(200,200,200,255)
        elif Gene_category == "Putative":
            SelectColor(Gene_category,120)
        else:
            SelectColor(Gene_category,255)

        if Gene_orientation == "+":
            rect(start_x+Gene_start/scale_x, start_y, (Gene_end-Gene_start)/scale_x, -15)
        else:
            rect(start_x+Gene_start/scale_x, start_y+15, (Gene_end-Gene_start)/scale_x, -15)
    
    ### Add grid lines to vertical axis
    
    for refval in [250, 500, 750, 1000, 1250, 1500]:
        strokeWeight(3)
        stroke(200,200,200)
        line(start_x, start_y+17+CalculateCoverage(refval)/scale_y, start_x+Ref_size/x_scale, start_y+17+CalculateCoverage(refval)/scale_y)
        line(start_x, start_y-13-CalculateCoverage(refval)/scale_y, start_x+Ref_size/x_scale, start_y-13-CalculateCoverage(refval)/scale_y)

    stroke(0)
    fill(0,0)
    strokeWeight(1)
    rect(start_x, start_y-15, Ref_size/scale_x, 30)

    for spec in SPEC_LIST:
        print("    Adding coverage for specimen %s" % spec)
        minus_str = workdir + spec + "_coverage_minus_strand.txt"

        COVTABLE = []
        TABLE = loadTable(minus_str, "tsv")
        for k in range(1, TABLE.getRowCount()):
            if TABLE.getRow(k).getString(0) == genome:
                COVTABLE.append([TABLE.getRow(k).getInt(1), TABLE.getRow(k).getInt(2)])

        #### Plotting total coverage (in bins corresponding to 1 pixel)

        pos_no = 0
        total_cov = 0
        pos_table = []
        strokeWeight(2)
        stroke(0,0,0)
        SelectColorSample(spec,75)
        beginShape()
        vertex(start_x, start_y-15)
        Ref_size = Ref_size - 1
        for pos in range(0, Ref_size):
            pos_no += 1
            total_cov += COVTABLE[pos][1]
            if pos_no == x_scale:
                average_cov = float(total_cov)/pos_no
                pos_table.append([pos, average_cov])
                vertex(start_x + pos/x_scale, start_y-15 - CalculateCoverage(average_cov)/scale_y)
                pos_no = 0
                total_cov = 0
        vertex(start_x + Ref_size/x_scale, start_y-15)
        endShape()

    for spec in SPEC_LIST:
        plus_str = workdir + spec + "_coverage_plus_strand.txt"
        COVTABLE = []
        TABLE = loadTable(plus_str, "tsv")
        for k in range(1, TABLE.getRowCount()):
            if TABLE.getRow(k).getString(0) == genome:
                COVTABLE.append([TABLE.getRow(k).getInt(1), TABLE.getRow(k).getInt(2)])
        #### Plotting total coverage (in bins corresponding to 1 pixel)
        pos_no = 0
        total_cov = 0
        pos_table = []
        strokeWeight(2)
        stroke(0,0,0)
        SelectColorSample(spec,75)
        beginShape()
        vertex(start_x, start_y+15)
        for pos in range(0, Ref_size):
            pos_no += 1
            total_cov += COVTABLE[pos][1]
            if pos_no == x_scale:
                average_cov = float(total_cov)/pos_no
                pos_table.append([pos, average_cov])
                vertex(start_x + pos/x_scale, start_y+15 + CalculateCoverage(average_cov)/scale_y)
                pos_no = 0
                total_cov = 0
        vertex(start_x + Ref_size/x_scale, start_y+15)
        endShape()


    ### Plotting vertical scale
    stroke(0)
    for refval in [0, 500, 1000, 1500]:
        strokeWeight(3)
        stroke(0,0,0)
        textAlign(RIGHT)
        fill(0)
        textSize(30)
        strokeWeight(0)
        text(refval, start_x - 10, start_y+21+CalculateCoverage(refval)/scale_y)
        text(refval, start_x - 10, start_y-9-CalculateCoverage(refval)/scale_y)

    ### Plotting horizontal scale
    for refval in range(0,Ref_size,10000):
        strokeWeight(3)
        line(start_x + refval/x_scale, start_y-15-330, start_x + refval/x_scale, start_y+15+330)
        textAlign(CENTER)
        text(str(refval/1000) + "k", start_x + refval/x_scale, start_y+30+345)


    ### Draw LEGEND
    fill(0)
    textAlign(LEFT)
    textSize(30)
    text("Gene category:", start_x + Ref_size/x_scale+50, start_y-90)
    textSize(20)
    text("Ribosomal RNA", start_x + Ref_size/x_scale+100, start_y-50)
    text("Ribosomal protein", start_x + Ref_size/x_scale+100, start_y-10)
    text("Chaperone", start_x + Ref_size/x_scale+100, start_y+30)
    text("Nutrient Biosynthesis", start_x + Ref_size/x_scale+100, start_y+70)
    text("tRNA", start_x + Ref_size/x_scale+100, start_y+110)
    text("Other", start_x + Ref_size/x_scale+100, start_y+150)
    text("Pseudogene", start_x + Ref_size/x_scale+100, start_y+190)

    SelectColor("rRNA", 255)
    rect(start_x + Ref_size/x_scale+50, start_y-50,40,-30)

    SelectColor("riboprot", 255)
    rect(start_x + Ref_size/x_scale+50, start_y-10,40,-30)

    SelectColor("chaperone", 255)
    rect(start_x + Ref_size/x_scale+50, start_y+30,40,-30)

    SelectColor("biosynth", 255)
    rect(start_x + Ref_size/x_scale+50, start_y+70,40,-30)

    SelectColor("tRNA", 255)
    rect(start_x + Ref_size/x_scale+50, start_y+110,40,-30)

    SelectColor("Other", 255)
    rect(start_x + Ref_size/x_scale+50, start_y+150,40,-30)

    stroke(200,200,200,255)
    fill(200,200,200,255)
    rect(start_x + Ref_size/x_scale+50, start_y+190,40,-30)

    textSize(48)
    fill(0)
    textAlign(LEFT)
    text(genome,40,60)

    println("Finished drawing plot!")
    endRecord()
