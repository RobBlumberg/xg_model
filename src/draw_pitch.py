def draw_pitch(rotate=False):
    line_width = 4
    alpha = 0.5
    r = 10
    
    line_coords = [[[0, 0], [0, 120]], [[0, 80], [120, 120]], [[80, 80], [120, 0]], [[0, 80], [0, 0]],
                       [[0, 80], [60, 60]], [[18, 18], [0, 18]], [[18, 62], [18, 18]], [[62, 62], [0, 18]],
                       [[30, 30], [0, 6]], [[30, 50], [6, 6]], [[50, 50], [0, 6]], [[18, 18], [120, 102]],
                       [[18, 62], [102, 102]], [[62, 62], [102, 120]], [[30, 30], [120, 114]],
                       [[30, 50], [114, 114]], [[50, 50], [120, 114]]]
    
    if not rotate:
        for lines in line_coords:               
            ax.plot(lines[0], lines[1], color = 'grey', linewidth = line_width, alpha = alpha)
        
        theta1 = np.linspace(0, 2*np.pi, 100)
        theta2 = np.linspace(0.65, 2.47, 100)
        theta3 = np.linspace(3.8, 5.6, 100)
        x1 = r*np.cos(theta1) + 40
        x2 = r*np.sin(theta1) + 60
        x3 = r*np.cos(theta2) + 40
        x4 = r*np.sin(theta2) + 12
        x5 = r*np.cos(theta3) + 40
        x6 = r*np.sin(theta3) + 108
        
        ax.plot(x1, x2, color = 'grey', linewidth = line_width, alpha = alpha)
        ax.plot(x3, x4, color = 'grey', linewidth = line_width, alpha = alpha)
        ax.plot(x5, x6, color = 'grey', linewidth = line_width, alpha = alpha)
        
    else:
        for lines in line_coords:               
            ax.plot([-(lines[1][0]-40) + 80, -(lines[1][1]-40) + 80], [lines[0][0], lines[0][1]], color = 'grey', 
                    linewidth = line_width, alpha = alpha)
        
        theta1 = np.linspace(0, 2*np.pi, 100)
        theta2 = np.linspace(5.4, 7.2, 100)
        theta3 = np.linspace(2.2, 4, 100)
        x1 = r*np.cos(theta1) + 60
        x2 = r*np.sin(theta1) + 40
        x3 = r*np.cos(theta2) + 12
        x4 = r*np.sin(theta2) + 40
        x5 = r*np.cos(theta3) + 108
        x6 = r*np.sin(theta3) + 40
        
        ax.plot(x1, x2, color = 'grey', linewidth = line_width, alpha = alpha)
        ax.plot(x3, x4, color = 'grey', linewidth = line_width, alpha = alpha)
        ax.plot(x5, x6, color = 'grey', linewidth = line_width, alpha = alpha)