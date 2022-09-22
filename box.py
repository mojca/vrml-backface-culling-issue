import cadquery as cq

box = cq.Workplane().box(2.0, 4.0, 1.0)
assy = cq.Assembly(box, loc=cq.Location((0,0,0)), color=cq.Color("black"))

cq.exporters.export(box, 'box-ok.wrl', cq.exporters.ExportTypes.VRML)
assy.save('box-has-back-face-culling-issues.wrl', exportType='VRML')
assy.save('box.step')
