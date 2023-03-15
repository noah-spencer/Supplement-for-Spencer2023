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

### List of contigs -- each is plotted separately.
GENOME_LIST = ["DICSEM"]

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
