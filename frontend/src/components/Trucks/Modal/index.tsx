import Button from 'react-bootstrap/Button';
import Modal from 'react-bootstrap/Modal';

type Props = {
    show: boolean,
    setShow: (valor:boolean)=>void,
    modalTitle:string,
    modalBody:string
}

function CardModal({show, setShow, modalTitle, modalBody}:Props) {
  const handleClose = () => setShow(false);

  return (

      <Modal show={show} onHide={handleClose}>
        <Modal.Header closeButton>
          <Modal.Title>{modalTitle}</Modal.Title>
        </Modal.Header>

        <Modal.Body>
          <p>{modalBody}</p>
        </Modal.Body>

        <Modal.Footer>
          <Button variant="secondary" onClick={handleClose}>Close</Button>
        </Modal.Footer>
      </Modal>
  );
}

export default CardModal;