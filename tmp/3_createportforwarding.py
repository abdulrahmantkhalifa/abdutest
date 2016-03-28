from JumpScale.portal.docgenerator.popup import Popup

def main(j, args, params, tags, tasklet):
	params.result = page = args.page
	cloudspaceId = int(args.getTag('cloudspaceId'))
	scl = j.clients.osis.getNamespace('cloudbroker')
	cloudspace = scl.cloudspace.get(cloudspaceId)
	#actors = j.apps.cloudbroker.iaas.cb.actors.cloudapi

	publicIP= cloudspace.publicipaddress
	vmachines = scl.vmachine.search({'cloudspaceId':cloudspaceId})[1:]
	dropvmachines = []

	def vmachinesorter(vmachine):
		return vmachine['name']
	for vmachines in sorted(vmachines, key=vmachinesorter):
		dropvmachines.append((vmachines['name'], vmachines['id']))


	popup = Popup(id='createPortForward', header='create PortForward', submit_url='/restmachine/cloudbroker/cloudspace/createPortForward')
    popup.addText('public Port', 'publicPort', required=True)
    popup.addText('local Port', 'localPort', required=True)
    popup.addDropdown('Choose Virtual Machine', 'vmid', dropvmachines)
    popup.addHiddenField('cloudspaceId', cloudspaceId)
    popup.addHiddenField('publicIp', publicIP)
    popup.write_html(page)


    return params

def match(j, args, params, tags, tasklet):
    return True