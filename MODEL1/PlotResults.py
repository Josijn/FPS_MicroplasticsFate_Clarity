import numpy as np
import matplotlib.pyplot as plt


def PlotResults(Concentrations_finalC_A1, Concentrations_finalC_B1,
                Concentrations_finalC_C1, Concentrations_finalC_D1,
                Concentrations_finalC_A2, Concentrations_finalC_B2, 
                Concentrations_finalC_C2, Concentrations_finalC_D2,
                Concentrations_finalC_A3, Concentrations_finalC_B3, 
                Concentrations_finalC_C3, Concentrations_finalC_D3, 
                Concentrations_finalC_A4, Concentrations_finalC_B4, 
                Concentrations_finalC_C4, Concentrations_finalC_D4, 
                t_span_final, compartments, MPforms):

    png_label1 = 'figures/' + compartments[0] + '.png'
    png_label2 = 'figures/' + compartments[1] + '.png'
    png_label3 = 'figures/' + compartments[2] + '.png'
    png_label4 = 'figures/' + compartments[3] + '.png'

    svg_label1 = 'figures/' + compartments[0] + '.svg'
    svg_label2 = 'figures/' + compartments[1] + '.svg'
    svg_label3 = 'figures/' + compartments[2] + '.svg'
    svg_label4 = 'figures/' + compartments[3] + '.svg'


    
    plt.figure(1)
    plt.title(compartments[0])
    plt.plot(t_span_final, Concentrations_finalC_A1[:], label= MPforms[0]);
    plt.plot(t_span_final, Concentrations_finalC_B1[:], label= MPforms[1]);
    plt.plot(t_span_final, Concentrations_finalC_C1[:], label= MPforms[2]);
    plt.plot(t_span_final, Concentrations_finalC_D1[:], label= MPforms[3]);
    plt.legend();
    plt.xlabel("time");
    plt.ylabel("concentration");
    plt.savefig(png_label1) #or pdf
    plt.savefig(svg_label1)
    plt.figure(2)
    plt.title(compartments[1])
    plt.plot(t_span_final, Concentrations_finalC_A2[:], label= MPforms[0]);
    plt.plot(t_span_final, Concentrations_finalC_B2[:], label= MPforms[1]);
    plt.plot(t_span_final, Concentrations_finalC_C2[:], label= MPforms[2]);
    plt.plot(t_span_final, Concentrations_finalC_D2[:], label= MPforms[3]);
    plt.legend();
    plt.xlabel("time");
    plt.ylabel("concentration");
    plt.savefig(png_label2) #or pdf
    plt.savefig(svg_label2)    
    plt.figure(3)
    plt.title(compartments[2])
    plt.plot(t_span_final, Concentrations_finalC_A3[:], label= MPforms[0]);
    plt.plot(t_span_final, Concentrations_finalC_B3[:], label= MPforms[1]);
    plt.plot(t_span_final, Concentrations_finalC_C3[:], label= MPforms[2]);
    plt.plot(t_span_final, Concentrations_finalC_D3[:], label= MPforms[3]);
    plt.legend();
    plt.xlabel("time");    
    plt.ylabel("concentration");
    plt.savefig(png_label3) #or pdf
    plt.savefig(svg_label3)
    plt.figure(4)
    plt.title(compartments[3])
    plt.plot(t_span_final, Concentrations_finalC_A4[:], label= MPforms[0]);
    plt.plot(t_span_final, Concentrations_finalC_B4[:], label= MPforms[1]);
    plt.plot(t_span_final, Concentrations_finalC_C4[:], label= MPforms[2]);
    plt.plot(t_span_final, Concentrations_finalC_D4[:], label= MPforms[3]);
    plt.legend();
    plt.xlabel("time");
    plt.ylabel("concentration");
    plt.savefig(png_label4) #or pdf
    plt.savefig(svg_label4)


def PlotResultsLogY(Concentrations_finalC_A1, Concentrations_finalC_B1,
                Concentrations_finalC_C1, Concentrations_finalC_D1,
                Concentrations_finalC_A2, Concentrations_finalC_B2, 
                Concentrations_finalC_C2, Concentrations_finalC_D2,
                Concentrations_finalC_A3, Concentrations_finalC_B3, 
                Concentrations_finalC_C3, Concentrations_finalC_D3, 
                Concentrations_finalC_A4, Concentrations_finalC_B4, 
                Concentrations_finalC_C4, Concentrations_finalC_D4, 
                t_span_final, compartments, MPforms):

    png_label1 = 'figures/' + compartments[0] + '_logY.png'
    png_label2 = 'figures/' + compartments[1] + '_logY.png'
    png_label3 = 'figures/' + compartments[2] + '_logY.png'
    png_label4 = 'figures/' + compartments[3] + '_logY.png'

    svg_label1 = 'figures/' + compartments[0] + '_logY.svg'
    svg_label2 = 'figures/' + compartments[1] + '_logY.svg'
    svg_label3 = 'figures/' + compartments[2] + '_logY.svg'
    svg_label4 = 'figures/' + compartments[3] + '_logY.svg'


    
    plt.figure(1)
    plt.title(compartments[0])
    plt.plot(t_span_final, Concentrations_finalC_A1[:], label= MPforms[0]);
    plt.plot(t_span_final, Concentrations_finalC_B1[:], label= MPforms[1]);
    plt.plot(t_span_final, Concentrations_finalC_C1[:], label= MPforms[2]);
    plt.plot(t_span_final, Concentrations_finalC_D1[:], label= MPforms[3]);
    plt.yscale("log")
    plt.legend();
    plt.xlabel("time");
    plt.ylabel("concentration");
    plt.savefig(png_label1) #or pdf
    plt.savefig(svg_label1)
    plt.figure(2)
    plt.title(compartments[1])
    plt.plot(t_span_final, Concentrations_finalC_A2[:], label= MPforms[0]);
    plt.plot(t_span_final, Concentrations_finalC_B2[:], label= MPforms[1]);
    plt.plot(t_span_final, Concentrations_finalC_C2[:], label= MPforms[2]);
    plt.plot(t_span_final, Concentrations_finalC_D2[:], label= MPforms[3]);
    plt.yscale("log")
    plt.legend();
    plt.xlabel("time");
    plt.ylabel("concentration");
    plt.savefig(png_label2) #or pdf
    plt.savefig(svg_label2)    
    plt.figure(3)
    plt.title(compartments[2])
    plt.plot(t_span_final, Concentrations_finalC_A3[:], label= MPforms[0]);
    plt.plot(t_span_final, Concentrations_finalC_B3[:], label= MPforms[1]);
    plt.plot(t_span_final, Concentrations_finalC_C3[:], label= MPforms[2]);
    plt.plot(t_span_final, Concentrations_finalC_D3[:], label= MPforms[3]);
    plt.yscale("log")
    plt.legend();
    plt.xlabel("time");    
    plt.ylabel("concentration");
    plt.savefig(png_label3) #or pdf
    plt.savefig(svg_label3)
    plt.figure(4)
    plt.title(compartments[3])
    plt.plot(t_span_final, Concentrations_finalC_A4[:], label= MPforms[0]);
    plt.plot(t_span_final, Concentrations_finalC_B4[:], label= MPforms[1]);
    plt.plot(t_span_final, Concentrations_finalC_C4[:], label= MPforms[2]);
    plt.plot(t_span_final, Concentrations_finalC_D4[:], label= MPforms[3]);
    plt.yscale("log")
    plt.legend();
    plt.xlabel("time");
    plt.ylabel("concentration");
    plt.savefig(png_label4) #or pdf
    plt.savefig(svg_label4)
    
    
    
    
